from enum import Enum, unique

@unique
class FTDI_COM_ERROR(Enum):
    #Error generated by from the FTDI or supporting code.
    FT_OK = 0x00
    FT_InvalidHandle = 0x01
    FT_DeviceNotFound = 0x02
    FT_DeviceNotOpened = 0X03
    FT_IOError = 0x04
    FT_InsufficientResources = 0x05
    FT_InvalidParameter = 0x06
    FT_DeviceNotPresent = 0x07
    FT_IncorrectDevice = 0x08

    #Errors generated by device Libraries.
    FT_NoDLLLoaded = 0x10
    FT_NoFunctionAvailable = 0x11
    FT_FunctionNotAvailable = 0x12
    FT_BadFunctionPointer = 0x13
    FT_GenericFunctionFail =0x14
    FT_SpecificFunctionFail = 0x15

    #The following errors are general errors generated by all DLLs.
    TL_ALREADY_OPEN = 0x20
    TL_NO_RESPONSE = 0x21
    TL_NOT_IMPLEMENTED = 0x22
    TL_FAULT_REPORTED = 0x23
    TL_INVALID_OPERATION = 0x24
    TL_DISCONNECTING = 0x28
    TL_FIRMWARE_BUG = 0x29
    TL_INITIALIZATION_FAILURE = 0x2a
    TL_INVALID_CHANNEL = 0x2b

    #The following errors are motor specific errors generated by the motor DDLs.
    TL_UNHOMED = 0x25
    TL_INVALID_POSITION = 0x26
    TL_INVALID_VELOCITY_PARAMETER = 0x27
    TL_CANNOT_HOME_DEVICE = 0x2c
    TL_JOG_CONTINOUS_MODE = 0x2d
    TL_NO_MOTOR_INFO = 0x2e
    TL_CMD_TEMP_UNAVAILABLE = 0x2f