"""Bluetooth Low Energy device abstraction
"""

from whad.ble.profile.service import Service
from whad.ble.profile.characteristic import CharacteristicDescriptor, CharacteristicProperties, Characteristic
from whad.ble.profile import GenericProfile
from whad.ble.stack.att.constants import BleAttProperties
from whad.ble.profile.attribute import UUID

class PeripheralCharacteristicDescriptor:

    def __init__(self, descriptor, gatt):
        self.__descriptor = descriptor
        self.__gatt = gatt

    @property
    def handle(self):
        return self.__descriptor.handle

    @property
    def type_uuid(self):
        return self.__descriptor.type_uuid

    def read(self):
        return self.__gatt.read(self.__descriptor.handle)

    def write(self, value, without_response=False):
        if without_response:
            self.__gatt.write_command(self.__descriptor.handle, value)
        else:
            self.__gatt.write(self.__descriptor.handle, value)

class PeripheralCharacteristic:
    """Characteristic wrapper for peripheral devices

    Instruments gatt to read/write a remote characteristic.
    """
    def __init__(self, characteristic, gatt):
        self.__characteristic = characteristic
        self.__gatt = gatt

    @property
    def value(self):
        """Transparent characteristic read

        :return bytes: Characteristic value
        """
        return self.read()

    @value.setter
    def value(self, val):
        """Transparent characteristic write

        :param bytes val: Value to write into this characteristic
        """
        return self.write(val)

    @property
    def uuid(self):
        return self.__characteristic.uuid

    @property
    def type_uuid(self):
        return self.__characteristic.type_uuid

    @property
    def properties(self):
        return self.__characteristic.properties

    @property
    def handle(self):
        return self.__characteristic.handle

    @property
    def end_handle(self):
        return self.__characteristic.end_handle

    @property
    def value_handle(self):
        return self.__characteristic.value_handle

    def read(self, offset=0):
        """Read characteristic value
        """
        if offset == 0:
            return self.__gatt.read(self.__characteristic.value_handle)
        else:
            return self.__gatt.read_blob(self.__characteristic.value_handle, offset)

    def read_long(self):
        """Read long characteristic value
        """
        return self.__gatt.read_long(self.__characteristic.value_handle)

    def write(self, value, without_response=False):
        """Set characteristic value

        TODO: handle prepared write !
        """
        if isinstance(value, bytes):
            if without_response:
                return self.__gatt.write_command(
                    self.__characteristic.value_handle,
                    value
                )
            else:
                return self.__gatt.write(
                    self.__characteristic.value_handle,
                    value
                )
        else:
            print('NOPE')

    def descriptors(self):
        for desc in self.__characteristic.descriptors():
            yield PeripheralCharacteristicDescriptor(
                desc,
                self.__gatt
            )

    def get_descriptor(self, type_uuid):
        """Get descriptor of a given type
        """
        for desc in self.__characteristic.descriptors():
            if desc.type_uuid == type_uuid:
                return PeripheralCharacteristicDescriptor(
                    desc,
                    self.__gatt
                )

    def readable(self):
        return ((self.__characteristic.properties & CharacteristicProperties.READ) != 0)

    def writeable(self):
        return (
            ((self.__characteristic.properties & CharacteristicProperties.WRITE) != 0) or 
            ((self.__characteristic.properties & CharacteristicProperties.WRITE_WITHOUT_RESPONSE) != 0)
        )

    def subscribe(self, notification=True, indication=False, callback=None):
        """Subscribe for notification/indication
        """
        if notification:
            # Look for CCCD
            desc = self.get_descriptor(UUID(0x2902))
            if desc is not None:
                # wrap our callback to provide more details about the concerned
                # characteristic
                def wrapped_cb(handle, value, indication=False):
                    callback(
                        self,
                        value,
                        indication=indication
                    )

                # Register our callback
                if callback is not None:
                    self.__gatt.register_notification_callback(
                        self.__characteristic.value_handle,
                        wrapped_cb
                    )

                # Enable notification
                desc.write(bytes([0x01, 0x00]))

                return True
            else:
                print('descriptor not found')
                return False
        elif indication:
            # Look for CCCD
            desc = self.get_descriptor(UUID(0x2902))
            if desc is not None:
                # Register our callback
                if callback is not None:
                    self.__gatt.register_notification_callback(
                        self.__characteristic.value_handle,
                        callback
                    )

                # Enable indication
                desc.write(bytes([0x02, 0x00]))

                return True
            else:
                return False
    
    def unsubscribe(self):
        """Unsubscribe to this characteristic
        """
        # Look for CCCD
        desc = self.get_descriptor(UUID(0x2902))

        if desc is not None:
            # Disable notification/indication
            desc.write(bytes([0x00, 0x00]))

            # Unregister our callback
            self.__gatt.unregister_notification_callback(
                self.__characteristic.value_handle
            )
            return True
        else:
            return False


class PeripheralService:
    """Service wrapper for peripheral devices
    """

    def __init__(self, service, gatt):
        self.__service = service
        self.__gatt = gatt

    @property
    def handle(self):
        return self.__service.handle

    @property
    def end_handle(self):
        return self.__service.end_handle

    @property
    def uuid(self):
        return self.__service.uuid

    @property
    def type_uuid(self):
        return self.__service.type_uuid

    def read_characteristic_by_uuid(self, uuid):
        return self.__gatt.read_characteristic_by_uuid(
            uuid,
            self.__service.handle,
            self.__service.end_handle
        )

    def get_characteristic(self, uuid):
        for charac in self.__service.characteristics():
            if charac.uuid == uuid:
                return PeripheralCharacteristic(
                    charac,
                    self.__gatt
                )
        return None

    def characteristics(self):
        for characteristic in self.__service.characteristics():
            yield PeripheralCharacteristic(
                characteristic,
                self.__gatt
            )

class PeripheralDevice(GenericProfile):
    """GATT client wrapper representing a remote device.

    This class is used to wrap a device model used in a gatt client
    in order to provide easy-to-use methods to access its services,
    characteristics and descriptors.
    """

    def __init__(self,  central, gatt_client, conn_handle, from_json=None):
        self.__gatt = gatt_client
        self.__conn_handle = conn_handle
        self.__central = central
        super().__init__(from_json=from_json)

    @property
    def conn_handle(self):
        return self.__conn_handle

    def disconnect(self):
        """Terminate the connection to this device
        """
        # Ask associated central to disconnect this peripheral device.
        self.__central.disconnect(self.__conn_handle)

    def discover(self):
        """Discovers services, characteristics and descriptors.

        This method must be called before accessing any service or characteristic,
        as it is required to retrieve the corresponding GATT handles.
        """
        # Discover
        self.__gatt.discover()

    def find_service_by_uuid(self, uuid):
        service = self.__gatt.discover_primary_service_by_uuid(uuid)
        if service is not None:
            return PeripheralService(
                service,
                self.__gatt
            )
        else:
            return None

    """
    def services(self):
        for service in super().services():
            yield PeripheralService(service, self.__gatt)
    """

    def find_object_by_handle(self, handle):
        obj = super().find_object_by_handle(handle)
        if isinstance(obj, Characteristic):
            return PeripheralCharacteristic(
                obj,
                self.__gatt
            )
        elif isinstance(obj, Service):
            return PeripheralService(
                obj,
                self.__gatt
            )

    def get_characteristic(self, service_uuid, charac_uuid):
        """Get a PeripheralCharacteristic object representing a characteristic
        defined by the given service UUID and characteristic UUID.

        :return: PeripheralCharacteristic object on success, None if not found.
        """
        service = self.get_service(service_uuid)
        if service is not None:
            return service.get_characteristic(charac_uuid)
        return None

    def get_service(self, uuid):
        """Retrieve a PeripheralService object given its UUID.
        """

        """
        for service in self.__gatt.services():
            if service.uuid == uuid:
                return PeripheralService(service, self.__gatt)
        return None
        """
        for service in self.services():
            if service.uuid == uuid:
                return PeripheralService(service, self.__gatt)
        return None

    


                    





    