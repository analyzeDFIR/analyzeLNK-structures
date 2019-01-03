## -*- coding: UTF-8 -*_
## lnk.py
##
## Copyright (c) 2018 analyzeDFIR
## 
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
## 
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
## 
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.

try:
    from constants import *
    from shared_structures.windows.guid import NTFSGUID
    from shared_structures.windows.misc import NTFSFILETIME
except ImportError:
    from .constants import *
    from .shared_structures.windows.guid import NTFSGUID
    from .shared_structures.windows.misc import NTFSFILETIME

LNKTrackerDataBlock = Struct(
    'Size'                          / Const(0x60, Int32ul),
    'Signature'                     / Const(b'\xA0\x00\x00\x03', Int32ul),
    'Length'                        / Const(0x58, Int32ul),
    'Version'                       / Const(0x00, Int32ul),
    # TODO: Figure out which string type and encoding to use, might be ASCII
    'MachineID'                     / PascalString(Bytes(16), 'utf16'),
    'RawDroidPart1'                 / NTFSGUID,
    'RawDroidPart2'                 / NTFSGUID,
    'RawDroidBirthPart1'            / NTFSGUID,
    'RawDroidBirthPart2'            / NTFSGUID
)

LNKSpecialFolderDataBlock = Struct(
    'Size'                          / Const(0x10, Int32ul),
    'Signature'                     / Const(b'\xA0\x00\x00\x05', Int32ul),
    'KnownFolderID'                 / Int32ul,
    'LinkTargetIDListOffset'        / Int32ul
)

LNKShimDataBlock = Struct(
    'Size'                          / Int32ul,
    'Signature'                     / Const(b'\xA0\x00\x00\x08', Int32ul),
    # TODO: Look in Construct API docs for Computed type, should be TotalSize - 8
    'LayerName'                     / Pass
)

LNKPropertyStoreDataBlock = Struct(
    'Size'                          / Int32ul,
    'Signature'                     / Const(b'\xA0\x00\x00\x09', Int32ul),
    # TODO: See MS-PROPSTORE to parse property store structure
    'PropertyStore'                 / Pass
)

LNKKnownFolderDataBlock = Struct(
    'Size'                          / Const(0x1C, Int32ul),
    'Signature'                     / Const(b'\xA0\x00\x00\x0B', Int32ul),
    'KnownFolderID'                 / NTFSGUID,
    'LinkTargetIDListOffset'        / Int32ul
)

LNKIconEnvironmentDataBlock = Struct(
    'Size'                          / Const(0x0314, Int32ul),
    'Signature'                     / Const(b'\xA0\x00\x00\x07', Int32ul),
    'RawTargetLocation'             / Bytes(260),
    'RawUTargetLocation'            / Bytes(520)
)

LNKEnvironmentVariablesDataBlock = Struct(
    'Size'                          / Const(0x0314, Int32ul),
    'Signature'                     / Const(b'\xA0\x00\x00\x01', Int32ul),
    'RawTargetLocation'             / Bytes(260),
    'RawUTargetLocation'            / Bytes(520)
)

LNKDarwinDataBlock = Struct(
    'Size'                          / Const(0x0314, Int32ul),
    'Signature'                     / Const(b'\xA0\x00\x00\x06', Int32ul),
    'RawApplicationIdentifier'      / Bytes(260),
    'RawUApplicationIdentifier'     / Bytes(520)
)

LNKConsoleFEDataBlock = Struct(
    'Size'                          / Const(0x0C, Int32ul),
    'Signature'                     / Const(b'\xA0\x00\x00\x04', Int32ul),
    # TODO: See MS-LCID for language code identifiers to build Enum
    'RawCodepage'                   / Int32ul
)

LNKConsoleDataBlock = Struct(
    'Size'                          / Const(0xCC, Int32ul),
    'Signature'                     / Const(b'\xA0\x00\x00\x02', Int32ul),
    'FillAttributes'                / LNKFillAttributesColors,
    'PopupFillAttributes'           / LNKFillAttributesColors,
    'ScreenBufferSizeX'             / Int16ul,
    'ScreenBufferSizeY'             / Int16ul,
    'WindowSizeX'                   / Int16ul,
    'WindowSizeY'                   / Int16ul,
    'WindowOriginX'                 / Int16ul,
    'WindowOriginY'                 / Int16ul,
    Padding(8),
    'FontSize'                      / Int32ul,
    'FontFamily'                    / Enum(Int32ul,
        FF_DONTCARE     = 0x00,
        FF_ROMAN        = 0x10,
        FW_SWISS        = 0x20,
        FF_MODERN       = 0x30,
        FF_SCRIPT       = 0x40,
        FF_DECORATIVE   = 0x50
    ),
    'FontWeight'                    / Int32ul,
    'RawFontFaceName'               / Bytes(64),
    'CursorSize'                    / Int32ul,
    'RawFullScreen'                 / Int32ul,
    'RawQuickEdit'                  / Int32ul,
    'RawInsertMode'                 / Int32ul,
    'RawAutomaticPosition'          / Int32ul,
    'HistoryBufferSize'             / Int32ul,
    'HistoryBufferCount'            / Int32ul,
    'RawHistoryDuplicatesAllowed'   / Int32ul,
    'RawColorTable'                 / Bytes(64)
)

LNKNetworkShareInformationHeader = Struct(
    'Size'                  / Int32ul,
    'Flags'                 / FlagsEnum(Int32ul,
        ValidDevice     = 0x01,
        ValidNetType    = 0x02
    ),
    'ShareNameOffset'       / Int32ul,
    'DeviceNameOffset'      / Int32ul,
    'NetworkProviderType'   / LNKNetworkProviderType,
    'UShareNameOffset'      / If(this.ShareNameOffset > 20, Int32ul),
    'UDeviceNameOffset'     / If(this.ShareNameOffset > 20, Int32ul)
)

LNKVolumeInformationHeader = Struct(
    'Size'                  / Int32ul,
    'DriveType'             / Enum(Int32ul,
        DRIVE_UNKNOWN       = 0x00,
        DRIVE_NO_ROOT_DIR   = 0x01,
        DRIVE_REMOVABLE     = 0x02,
        DRIVE_FIXED         = 0x03,
        DRIVE_REMOTE        = 0x04,
        DRIVE_CDROM         = 0x05,
        DRIVE_RAMDISK       = 0x06
    ),
    'DriveSerialNumber'     / Int32ul,
    'VolumeLabelOffset'     / Int32ul,
    'UVolumeLabelOffset'    / If(this.VolumeLabelOffset > 16, Int32ul)
)

LNKLocationInformationHeader = Struct(
    'Size'                              / Int32ul,
    'HeaderSize'                        / Int32ul,
    'Flags'                             / FlagsEnum(Int32ul,
        VolumeIDAndLocalBasePath                = 0x01,
        CommonNetworkRelativeLinkAndPathSuffix  = 0x02
    ),
    'VolumeIDOffset'                    / Int32ul,
    'LocalBasePathOffset'               / Int32ul,
    'CommonNetworkRelativeLinkOffset'   / Int32ul,
    'CommonPathSuffixOffset'            / Int32ul,
    'ULocalBasePathOffset'              / If(this.HeaderSize > 28, Int32ul),
    'UCommonPathSuffixOffset'           / If(this.HeaderSize > 32, Int32ul)
)

LNKLinkTargetIDListItemID = Struct(
    'Size'                  / Int16ul,
    'Data'                  / Bytes(this.Size - 2)
)

LNKLinkTargetIDListSize = Int16ul

LNKHotKey = Struct(
    'LowerValue'            / LNKHotKeyLowerValue,
    'UpperValue'            / LNKHotKeyUpperValue
)

LNKFileHeader = Struct(
    'HeaderSize'            / Const(0x4C, Int32ul),
    'LNKClassIdentifier'    / NTFSGUID,
    'DataFlags'             / LNKDataFlags,
    'FileAttributeFlags'    / Int32ul,
    'RawCreateTime'         / NTFSFILETIME,
    'RawLastAccessTime'     / NTFSFILETIME,
    'RawLastModifiedTime'   / NTFSFILETIME,
    'FileSize'              / Int32ul,
    'IconIndex'             / Int32sl,
    'ShowWindow'            / LNKShowWindow,
    'HotKey'                / LNKHotKey,
    Padding(10)
)
