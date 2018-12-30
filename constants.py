## -*- coding: UTF-8 -*_
## constants.py
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

from construct import *

LNKFillAttributesColors = FlagsEnum(Int16ul,
    FOREGROUND_BLUE         = 0x01,
    FOREGROUND_GREEN        = 0x02,
    FOREGROUND_RED          = 0x04,
    FOREGROUND_INTENSITY    = 0x08,
    BACKGROUND_BLUE         = 0x10,
    BACKGROUND_GREEN        = 0x20,
    BACKGROUND_RED          = 0x40,
    BACKGROUND_INTENSITY    = 0x80
)

LNKNetworkProviderType = Enum(Int32ul,
    WNNC_NET_AVID           = 0x001a0000,
    WNNC_NET_DOCUSPACE	    = 0x001b0000,
    WNNC_NET_MANGOSOFT	    = 0x001c0000,
    WNNC_NET_SERNET	        = 0x001d0000,
    WNNC_NET_RIVERFRONT1	= 0x001e0000,
    WNNC_NET_RIVERFRONT2	= 0x001f0000,
    WNNC_NET_DECORB	        = 0x00200000,
    WNNC_NET_PROTSTOR	    = 0x00210000,
    WNNC_NET_FJ_REDIR	    = 0x00220000,
    WNNC_NET_DISTINCT	    = 0x00230000,
    WNNC_NET_TWINS	        = 0x00240000,
    WNNC_NET_RDR2SAMPLE	    = 0x00250000,
    WNNC_NET_CSC	        = 0x00260000,
    WNNC_NET_3IN1	        = 0x00270000,
    WNNC_NET_EXTENDNET	    = 0x00290000,
    WNNC_NET_STAC	        = 0x002a0000,
    WNNC_NET_FOXBAT	        = 0x002b0000,
    WNNC_NET_YAHOO	        = 0x002c0000,
    WNNC_NET_EXIFS	        = 0x002d0000,
    WNNC_NET_DAV	        = 0x002e0000,
    WNNC_NET_KNOWARE	    = 0x002f0000,
    WNNC_NET_OBJECT_DIRE	= 0x00300000,
    WNNC_NET_MASFAX	        = 0x00310000,
    WNNC_NET_HOB_NFS	    = 0x00320000,
    WNNC_NET_SHIVA	        = 0x00330000,
    WNNC_NET_IBMAL	        = 0x00340000,
    WNNC_NET_LOCK	        = 0x00350000,
    WNNC_NET_TERMSRV	    = 0x00360000,
    WNNC_NET_SRT	        = 0x00370000,
    WNNC_NET_QUINCY	        = 0x00380000,
    WNNC_NET_OPENAFS	    = 0x00390000,
    WNNC_NET_AVID1	        = 0x003a0000,
    WNNC_NET_DFS	        = 0x003b0000,
    WNNC_NET_KWNP	        = 0x003c0000,
    WNNC_NET_ZENWORKS	    = 0x003d0000,
    WNNC_NET_DRIVEONWEB	    = 0x003e0000,
    WNNC_NET_VMWARE	        = 0x003f0000,
    WNNC_NET_RSFX	        = 0x00400000,
    WNNC_NET_MFILES	        = 0x00410000,
    WNNC_NET_MS_NFS	        = 0x00420000,
    WNNC_NET_GOOGLE	        = 0x00430000
)

LNKHotKeyUpperValue = Enum(Int8ul,
    NOKEY                   = 0x00,
    HOTKEYF_SHIFT           = 0x01,
    HOTKEYF_CONTROL         = 0x02,
    HOTKEYF_ALT             = 0x03
)

'''
LNK Hot Key Virtual Keys
NOTE:
    See https://docs.microsoft.com/en-us/windows/desktop/inputdev/virtual-key-codes
'''
LNKHotKeyLowerValue = Enum(Int8ul,
    NOKEY                   = 0x00,
    VK_00                   = 0x30,
    VK_01                   = 0x31,
    VK_02                   = 0x32,
    VK_03                   = 0x33,
    VK_04                   = 0x34,
    VK_05                   = 0x35,
    VK_06                   = 0x36,
    VK_07                   = 0x37,
    VK_08                   = 0x38,
    VK_09                   = 0x39,
    VK_A                    = 0x41, 
    VK_B                    = 0x42,
    VK_C                    = 0x43,
    VK_D                    = 0x44,
    VK_E                    = 0x45,
    VK_F                    = 0x46,
    VK_G                    = 0x47,
    VK_H                    = 0x48,
    VK_I                    = 0x49,
    VK_J                    = 0x4A,
    VK_K                    = 0x4B,
    VK_L                    = 0x4C,
    VK_M                    = 0x4D,
    VK_N                    = 0x4E,
    VK_O                    = 0x4F,
    VK_P                    = 0x50,
    VK_Q                    = 0x51,
    VK_R                    = 0x52,
    VK_S                    = 0x53,
    VK_T                    = 0x54,
    VK_U                    = 0x55,
    VK_V                    = 0x56,
    VK_W                    = 0x57,
    VK_X                    = 0x58,
    VK_Y                    = 0x59,
    VK_Z                    = 0x5A,
    VK_F1                   = 0x70,
    VK_F2                   = 0x71,
    VK_F3                   = 0x72,
    VK_F4                   = 0x73,
    VK_F5                   = 0x74,
    VK_F6                   = 0x75,
    VK_F7                   = 0x76,
    VK_F8                   = 0x77,
    VK_F9                   = 0x78,
    VK_F10                  = 0x79,
    VK_F11                  = 0x7a,
    VK_F12                  = 0x7b,
    VK_F13                  = 0x7c,
    VK_F14                  = 0x7d,
    VK_F15                  = 0x7e,
    VK_F16                  = 0x7f,
    VK_F17                  = 0x80,
    VK_F18                  = 0x81,
    VK_F19                  = 0x82,
    VK_F20                  = 0x83,
    VK_F21                  = 0x84,
    VK_F22                  = 0x85,
    VK_F23                  = 0x86,
    VK_F24                  = 0x87,
    VK_NUMLOCK              = 0x90,
    VK_SCROLL               = 0x91
)

'''
LNK Show Window: value used by the ShowWindow function
NOTE: 
    See https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-showwindow
'''
LNKShowWindow = Enum(Int32ul,
    SW_HIDE                 = 0x00,
    SW_SHOWNORMAL           = 0x01,
    SW_SHOWMINIMIZED        = 0x02,
    SW_SHOWMAXIMIZED        = 0x03,
    SW_SHOWNOACTIVATE       = 0x04,
    SW_SHOW                 = 0x05,
    SW_MINIMIZE             = 0x06,
    SW_SHOWMINNOACTIVE      = 0x07,
    SW_SHOWNA               = 0x08,
    SW_RESTORE              = 0x09,
    SW_SHOWDEFAULT          = 0x0A,
    SW_FORCEMINIMIZE        = 0x0B,
    SW_NORMALNA             = 0xCC
)

'''
LNK File Data Flags
NOTE:
    See https://github.com/libyal/liblnk/blob/master/documentation/Windows%20Shortcut%20File%20(LNK)%20format.asciidoc
'''
LNKDataFlags = FlagsEnum(Int32ul, 
    HasTargetIDList             = 0x00000001,
    HasLinkInfo                 = 0x00000002,
    HasName                     = 0x00000004,
    HasRelativePath             = 0x00000008,
    HasWorkingDir               = 0x00000010,
    HasArguments                = 0x00000020,
    HasIconLocation             = 0x00000040,
    IsUnicode                   = 0x00000080,
    ForceNoLinkInfo             = 0x00000100,
    HasExpString                = 0x00000200,
    RunInSeparateProcess        = 0x00000400,
    HasDarwinID                 = 0x00001000,
    RunAsUser                   = 0x00002000,
    HasExpIcon                  = 0x00004000,
    NoPidlAlias                 = 0x00008000,
    RunWithShimLayer            = 0x00020000,
    ForceNoLinkTrack            = 0x00040000,
    EnableTargetMetadata        = 0x00080000,
    DisableLinkPathTracking     = 0x00100000,
    DisableKnownFolderTracking  = 0x00200000,
    DisableKnownFolderAlias     = 0x00400000,
    AllowLinkToLink             = 0x00800000,
    UnaliasOnSave               = 0x01000000,
    PreferEnvironmentPath       = 0x02000000,
    KeepLocalIDListForUNCTarget = 0x04000000,
)
