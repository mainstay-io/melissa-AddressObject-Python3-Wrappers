from ctypes import *
from enum import Enum
import ctypes
import os
import sys

if (os.name == 'nt' and sys.version_info[:2] >= (3,8)):
  lib = ctypes.CDLL('mdAddr.dll', winmode=0)
elif (os.name == 'nt'):
  lib = ctypes.CDLL('mdAddr.dll')
else:
  # OX has patched the commented out code to support loading the library
  # from a custom path, as we load multiple versions.
  # lib = ctypes.CDLL('libmdAddr.so')
  lib_path = os.environ['MELISSA_LD_LIBRARY_PATH']
  lib = ctypes.CDLL(os.path.join(lib_path, 'libmdAddr.so'))

lib.mdAddrCreate.argtypes = []
lib.mdAddrCreate.restype = c_void_p
lib.mdAddrDestroy.argtypes = [c_void_p]
lib.mdAddrDestroy.restype = None
lib.mdAddrInitialize.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p]
lib.mdAddrInitialize.restype = c_int
lib.mdAddrInitializeDataFiles.argtypes = [c_void_p]
lib.mdAddrInitializeDataFiles.restype = c_int
lib.mdAddrGetInitializeErrorString.argtypes = [c_void_p]
lib.mdAddrGetInitializeErrorString.restype = c_char_p
lib.mdAddrSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetLicenseString.restype = c_bool
lib.mdAddrGetBuildNumber.argtypes = [c_void_p]
lib.mdAddrGetBuildNumber.restype = c_char_p
lib.mdAddrGetDatabaseDate.argtypes = [c_void_p]
lib.mdAddrGetDatabaseDate.restype = c_char_p
lib.mdAddrGetExpirationDate.argtypes = [c_void_p]
lib.mdAddrGetExpirationDate.restype = c_char_p
lib.mdAddrGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdAddrGetLicenseExpirationDate.restype = c_char_p
lib.mdAddrGetCanadianDatabaseDate.argtypes = [c_void_p]
lib.mdAddrGetCanadianDatabaseDate.restype = c_char_p
lib.mdAddrGetCanadianExpirationDate.argtypes = [c_void_p]
lib.mdAddrGetCanadianExpirationDate.restype = c_char_p
lib.mdAddrSetPathToUSFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToUSFiles.restype = None
lib.mdAddrSetPathToCanadaFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToCanadaFiles.restype = None
lib.mdAddrSetPathToDPVDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToDPVDataFiles.restype = None
lib.mdAddrSetPathToLACSLinkDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToLACSLinkDataFiles.restype = None
lib.mdAddrSetPathToSuiteLinkDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToSuiteLinkDataFiles.restype = None
lib.mdAddrSetPathToSuiteFinderDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToSuiteFinderDataFiles.restype = None
lib.mdAddrSetPathToRBDIFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToRBDIFiles.restype = None
lib.mdAddrGetRBDIDatabaseDate.argtypes = [c_void_p]
lib.mdAddrGetRBDIDatabaseDate.restype = c_char_p
lib.mdAddrSetPathToAddrKeyDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToAddrKeyDataFiles.restype = None
lib.mdAddrClearProperties.argtypes = [c_void_p]
lib.mdAddrClearProperties.restype = None
lib.mdAddrResetDPV.argtypes = [c_void_p]
lib.mdAddrResetDPV.restype = None
lib.mdAddrSetCASSEnable.argtypes = [c_void_p, c_int]
lib.mdAddrSetCASSEnable.restype = None
lib.mdAddrSetUseUSPSPreferredCityNames.argtypes = [c_void_p, c_int]
lib.mdAddrSetUseUSPSPreferredCityNames.restype = None
lib.mdAddrSetDiacritics.argtypes = [c_void_p, c_int]
lib.mdAddrSetDiacritics.restype = None
lib.mdAddrGetStatusCode.argtypes = [c_void_p]
lib.mdAddrGetStatusCode.restype = c_char_p
lib.mdAddrGetErrorCode.argtypes = [c_void_p]
lib.mdAddrGetErrorCode.restype = c_char_p
lib.mdAddrGetErrorString.argtypes = [c_void_p]
lib.mdAddrGetErrorString.restype = c_char_p
lib.mdAddrGetResults.argtypes = [c_void_p]
lib.mdAddrGetResults.restype = c_char_p
lib.mdAddrGetResultCodeDescription.argtypes = [c_void_p, c_char_p, c_int]
lib.mdAddrGetResultCodeDescription.restype = c_char_p
lib.mdAddrSetPS3553_B1_ProcessorName.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_B1_ProcessorName.restype = None
lib.mdAddrSetPS3553_B4_ListName.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_B4_ListName.restype = None
lib.mdAddrSetPS3553_D3_Name.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_D3_Name.restype = None
lib.mdAddrSetPS3553_D3_Company.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_D3_Company.restype = None
lib.mdAddrSetPS3553_D3_Address.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_D3_Address.restype = None
lib.mdAddrSetPS3553_D3_City.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_D3_City.restype = None
lib.mdAddrSetPS3553_D3_State.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_D3_State.restype = None
lib.mdAddrSetPS3553_D3_ZIP.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_D3_ZIP.restype = None
lib.mdAddrGetFormPS3553.argtypes = [c_void_p]
lib.mdAddrGetFormPS3553.restype = c_char_p
lib.mdAddrSaveFormPS3553.argtypes = [c_void_p, c_char_p]
lib.mdAddrSaveFormPS3553.restype = c_bool
lib.mdAddrResetFormPS3553.argtypes = [c_void_p]
lib.mdAddrResetFormPS3553.restype = None
lib.mdAddrResetFormPS3553Counter.argtypes = [c_void_p]
lib.mdAddrResetFormPS3553Counter.restype = None
lib.mdAddrSetStandardizationType.argtypes = [c_void_p, c_int]
lib.mdAddrSetStandardizationType.restype = None
lib.mdAddrSetSuiteParseMode.argtypes = [c_void_p, c_int]
lib.mdAddrSetSuiteParseMode.restype = None
lib.mdAddrSetAliasMode.argtypes = [c_void_p, c_int]
lib.mdAddrSetAliasMode.restype = None
lib.mdAddrGetFormSOA.argtypes = [c_void_p]
lib.mdAddrGetFormSOA.restype = c_char_p
lib.mdAddrSaveFormSOA.argtypes = [c_void_p, c_char_p]
lib.mdAddrSaveFormSOA.restype = None
lib.mdAddrResetFormSOA.argtypes = [c_void_p]
lib.mdAddrResetFormSOA.restype = None
lib.mdAddrSetSOACustomerInfo.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdAddrSetSOACustomerInfo.restype = None
lib.mdAddrSetSOACPCNumber.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetSOACPCNumber.restype = None
lib.mdAddrGetSOACustomerInfo.argtypes = [c_void_p]
lib.mdAddrGetSOACustomerInfo.restype = c_char_p
lib.mdAddrGetSOACPCNumber.argtypes = [c_void_p]
lib.mdAddrGetSOACPCNumber.restype = c_char_p
lib.mdAddrGetSOATotalRecords.argtypes = [c_void_p]
lib.mdAddrGetSOATotalRecords.restype = c_long
lib.mdAddrGetSOAAAPercentage.argtypes = [c_void_p]
lib.mdAddrGetSOAAAPercentage.restype = c_float
lib.mdAddrGetSOAAAExpiryDate.argtypes = [c_void_p]
lib.mdAddrGetSOAAAExpiryDate.restype = c_char_p
lib.mdAddrGetSOASoftwareInfo.argtypes = [c_void_p]
lib.mdAddrGetSOASoftwareInfo.restype = c_char_p
lib.mdAddrGetSOAErrorString.argtypes = [c_void_p]
lib.mdAddrGetSOAErrorString.restype = c_char_p
lib.mdAddrSetCompany.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetCompany.restype = None
lib.mdAddrSetLastName.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetLastName.restype = None
lib.mdAddrSetAddress.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetAddress.restype = None
lib.mdAddrSetAddress2.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetAddress2.restype = None
lib.mdAddrSetLastLine.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetLastLine.restype = None
lib.mdAddrSetSuite.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetSuite.restype = None
lib.mdAddrSetCity.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetCity.restype = None
lib.mdAddrSetState.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetState.restype = None
lib.mdAddrSetZip.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetZip.restype = None
lib.mdAddrSetPlus4.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPlus4.restype = None
lib.mdAddrSetUrbanization.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetUrbanization.restype = None
lib.mdAddrSetParsedAddressRange.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedAddressRange.restype = None
lib.mdAddrSetParsedPreDirection.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedPreDirection.restype = None
lib.mdAddrSetParsedStreetName.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedStreetName.restype = None
lib.mdAddrSetParsedSuffix.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedSuffix.restype = None
lib.mdAddrSetParsedPostDirection.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedPostDirection.restype = None
lib.mdAddrSetParsedSuiteName.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedSuiteName.restype = None
lib.mdAddrSetParsedSuiteRange.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedSuiteRange.restype = None
lib.mdAddrSetParsedRouteService.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedRouteService.restype = None
lib.mdAddrSetParsedLockBox.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedLockBox.restype = None
lib.mdAddrSetParsedDeliveryInstallation.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedDeliveryInstallation.restype = None
lib.mdAddrSetCountryCode.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetCountryCode.restype = None
lib.mdAddrVerifyAddress.argtypes = [c_void_p]
lib.mdAddrVerifyAddress.restype = c_bool
lib.mdAddrGetCompany.argtypes = [c_void_p]
lib.mdAddrGetCompany.restype = c_char_p
lib.mdAddrGetLastName.argtypes = [c_void_p]
lib.mdAddrGetLastName.restype = c_char_p
lib.mdAddrGetAddress.argtypes = [c_void_p]
lib.mdAddrGetAddress.restype = c_char_p
lib.mdAddrGetAddress2.argtypes = [c_void_p]
lib.mdAddrGetAddress2.restype = c_char_p
lib.mdAddrGetSuite.argtypes = [c_void_p]
lib.mdAddrGetSuite.restype = c_char_p
lib.mdAddrGetCity.argtypes = [c_void_p]
lib.mdAddrGetCity.restype = c_char_p
lib.mdAddrGetCityAbbreviation.argtypes = [c_void_p]
lib.mdAddrGetCityAbbreviation.restype = c_char_p
lib.mdAddrGetState.argtypes = [c_void_p]
lib.mdAddrGetState.restype = c_char_p
lib.mdAddrGetZip.argtypes = [c_void_p]
lib.mdAddrGetZip.restype = c_char_p
lib.mdAddrGetPlus4.argtypes = [c_void_p]
lib.mdAddrGetPlus4.restype = c_char_p
lib.mdAddrGetCarrierRoute.argtypes = [c_void_p]
lib.mdAddrGetCarrierRoute.restype = c_char_p
lib.mdAddrGetDeliveryPointCode.argtypes = [c_void_p]
lib.mdAddrGetDeliveryPointCode.restype = c_char_p
lib.mdAddrGetDeliveryPointCheckDigit.argtypes = [c_void_p]
lib.mdAddrGetDeliveryPointCheckDigit.restype = c_char_p
lib.mdAddrGetCountyFips.argtypes = [c_void_p]
lib.mdAddrGetCountyFips.restype = c_char_p
lib.mdAddrGetCountyName.argtypes = [c_void_p]
lib.mdAddrGetCountyName.restype = c_char_p
lib.mdAddrGetAddressTypeCode.argtypes = [c_void_p]
lib.mdAddrGetAddressTypeCode.restype = c_char_p
lib.mdAddrGetAddressTypeString.argtypes = [c_void_p]
lib.mdAddrGetAddressTypeString.restype = c_char_p
lib.mdAddrGetUrbanization.argtypes = [c_void_p]
lib.mdAddrGetUrbanization.restype = c_char_p
lib.mdAddrGetCongressionalDistrict.argtypes = [c_void_p]
lib.mdAddrGetCongressionalDistrict.restype = c_char_p
lib.mdAddrGetLACS.argtypes = [c_void_p]
lib.mdAddrGetLACS.restype = c_char_p
lib.mdAddrGetLACSLinkIndicator.argtypes = [c_void_p]
lib.mdAddrGetLACSLinkIndicator.restype = c_char_p
lib.mdAddrGetPrivateMailbox.argtypes = [c_void_p]
lib.mdAddrGetPrivateMailbox.restype = c_char_p
lib.mdAddrGetTimeZoneCode.argtypes = [c_void_p]
lib.mdAddrGetTimeZoneCode.restype = c_char_p
lib.mdAddrGetTimeZone.argtypes = [c_void_p]
lib.mdAddrGetTimeZone.restype = c_char_p
lib.mdAddrGetMsa.argtypes = [c_void_p]
lib.mdAddrGetMsa.restype = c_char_p
lib.mdAddrGetPmsa.argtypes = [c_void_p]
lib.mdAddrGetPmsa.restype = c_char_p
lib.mdAddrGetDefaultFlagIndicator.argtypes = [c_void_p]
lib.mdAddrGetDefaultFlagIndicator.restype = c_char_p
lib.mdAddrGetSuiteStatus.argtypes = [c_void_p]
lib.mdAddrGetSuiteStatus.restype = c_char_p
lib.mdAddrGetEWSFlag.argtypes = [c_void_p]
lib.mdAddrGetEWSFlag.restype = c_char_p
lib.mdAddrGetCMRA.argtypes = [c_void_p]
lib.mdAddrGetCMRA.restype = c_char_p
lib.mdAddrGetDsfVacant.argtypes = [c_void_p]
lib.mdAddrGetDsfVacant.restype = c_char_p
lib.mdAddrGetCountryCode.argtypes = [c_void_p]
lib.mdAddrGetCountryCode.restype = c_char_p
lib.mdAddrGetZipType.argtypes = [c_void_p]
lib.mdAddrGetZipType.restype = c_char_p
lib.mdAddrGetFalseTable.argtypes = [c_void_p]
lib.mdAddrGetFalseTable.restype = c_char_p
lib.mdAddrGetDPVFootnotes.argtypes = [c_void_p]
lib.mdAddrGetDPVFootnotes.restype = c_char_p
lib.mdAddrGetLACSLinkReturnCode.argtypes = [c_void_p]
lib.mdAddrGetLACSLinkReturnCode.restype = c_char_p
lib.mdAddrGetSuiteLinkReturnCode.argtypes = [c_void_p]
lib.mdAddrGetSuiteLinkReturnCode.restype = c_char_p
lib.mdAddrGetRBDI.argtypes = [c_void_p]
lib.mdAddrGetRBDI.restype = c_char_p
lib.mdAddrGetELotNumber.argtypes = [c_void_p]
lib.mdAddrGetELotNumber.restype = c_char_p
lib.mdAddrGetELotOrder.argtypes = [c_void_p]
lib.mdAddrGetELotOrder.restype = c_char_p
lib.mdAddrGetAddressKey.argtypes = [c_void_p]
lib.mdAddrGetAddressKey.restype = c_char_p
lib.mdAddrGetMelissaAddressKey.argtypes = [c_void_p]
lib.mdAddrGetMelissaAddressKey.restype = c_char_p
lib.mdAddrGetMelissaAddressKeyBase.argtypes = [c_void_p]
lib.mdAddrGetMelissaAddressKeyBase.restype = c_char_p
if os.environ['DQS_VERSION'] >= 'dqs.202306':
  # GetOutputParameter is new in dqs.202306
  # https://releasenotes.melissa.com/on-premise-api/address-object/#202306
  lib.mdAddrGetOutputParameter.argtypes = [c_void_p, c_char_p]
  lib.mdAddrGetOutputParameter.restype = c_char_p
  lib.mdAddrSetInputParameter.argtypes = [c_void_p, c_char_p, c_char_p]
  lib.mdAddrSetInputParameter.restype = c_int
lib.mdAddrFindSuggestion.argtypes = [c_void_p]
lib.mdAddrFindSuggestion.restype = c_bool
lib.mdAddrFindSuggestionNext.argtypes = [c_void_p]
lib.mdAddrFindSuggestionNext.restype = c_bool
lib.mdAddrGetDsfNoStats.argtypes = [c_void_p]
lib.mdAddrGetDsfNoStats.restype = c_char_p
if os.environ['DQS_VERSION'] >= 'dqs.202106':
  # GetDsfDNA fails prior to dqs.202106.
  #   AttributeError: /melissa_data/dqs.202105/address/linux/gcc41_64bit/libmdAddr.so: undefined symbol:
  #   mdAddrGetDsfDNA. Did you mean: 'mdAddrGetMsa'?
  lib.mdAddrGetDsfDNA.argtypes = [c_void_p]
  lib.mdAddrGetDsfDNA.restype = c_char_p
lib.mdAddrGetPS3553_B6_TotalRecords.argtypes = [c_void_p]
lib.mdAddrGetPS3553_B6_TotalRecords.restype = c_int
lib.mdAddrGetPS3553_C1a_ZIP4Coded.argtypes = [c_void_p]
lib.mdAddrGetPS3553_C1a_ZIP4Coded.restype = c_int
lib.mdAddrGetPS3553_C1c_DPBCAssigned.argtypes = [c_void_p]
lib.mdAddrGetPS3553_C1c_DPBCAssigned.restype = c_int
lib.mdAddrGetPS3553_C1d_FiveDigitCoded.argtypes = [c_void_p]
lib.mdAddrGetPS3553_C1d_FiveDigitCoded.restype = c_int
lib.mdAddrGetPS3553_C1e_CRRTCoded.argtypes = [c_void_p]
lib.mdAddrGetPS3553_C1e_CRRTCoded.restype = c_int
lib.mdAddrGetPS3553_C1f_eLOTAssigned.argtypes = [c_void_p]
lib.mdAddrGetPS3553_C1f_eLOTAssigned.restype = c_int
lib.mdAddrGetPS3553_E_HighRiseDefault.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_HighRiseDefault.restype = c_int
lib.mdAddrGetPS3553_E_HighRiseExact.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_HighRiseExact.restype = c_int
lib.mdAddrGetPS3553_E_RuralRouteDefault.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_RuralRouteDefault.restype = c_int
lib.mdAddrGetPS3553_E_RuralRouteExact.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_RuralRouteExact.restype = c_int
lib.mdAddrGetZip4HRDefault.argtypes = [c_void_p]
lib.mdAddrGetZip4HRDefault.restype = c_int
lib.mdAddrGetZip4HRExact.argtypes = [c_void_p]
lib.mdAddrGetZip4HRExact.restype = c_int
lib.mdAddrGetZip4RRDefault.argtypes = [c_void_p]
lib.mdAddrGetZip4RRDefault.restype = c_int
lib.mdAddrGetZip4RRExact.argtypes = [c_void_p]
lib.mdAddrGetZip4RRExact.restype = c_int
lib.mdAddrGetPS3553_E_LACSCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_LACSCount.restype = c_int
lib.mdAddrGetPS3553_E_EWSCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_EWSCount.restype = c_int
lib.mdAddrGetPS3553_E_DPVCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_DPVCount.restype = c_int
lib.mdAddrGetPS3553_X_POBoxCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_POBoxCount.restype = c_int
lib.mdAddrGetPS3553_X_HCExactCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_HCExactCount.restype = c_int
lib.mdAddrGetPS3553_X_FirmCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_FirmCount.restype = c_int
lib.mdAddrGetPS3553_X_GenDeliveryCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_GenDeliveryCount.restype = c_int
lib.mdAddrGetPS3553_X_MilitaryZipCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_MilitaryZipCount.restype = c_int
lib.mdAddrGetPS3553_X_NonDeliveryCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_NonDeliveryCount.restype = c_int
lib.mdAddrGetPS3553_X_StreetCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_StreetCount.restype = c_int
lib.mdAddrGetPS3553_X_HCDefaultCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_HCDefaultCount.restype = c_int
lib.mdAddrGetPS3553_X_OtherCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_OtherCount.restype = c_int
lib.mdAddrGetPS3553_X_LacsLinkCodeACount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_LacsLinkCodeACount.restype = c_int
lib.mdAddrGetPS3553_X_LacsLinkCode00Count.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_LacsLinkCode00Count.restype = c_int
lib.mdAddrGetPS3553_X_LacsLinkCode14Count.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_LacsLinkCode14Count.restype = c_int
lib.mdAddrGetPS3553_X_LacsLinkCode92Count.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_LacsLinkCode92Count.restype = c_int
lib.mdAddrGetPS3553_X_LacsLinkCode09Count.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_LacsLinkCode09Count.restype = c_int
lib.mdAddrGetPS3553_X_SuiteLinkCodeACount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_SuiteLinkCodeACount.restype = c_int
lib.mdAddrGetPS3553_X_SuiteLinkCode00Count.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_SuiteLinkCode00Count.restype = c_int
lib.mdAddrGetParsedAddressRange.argtypes = [c_void_p]
lib.mdAddrGetParsedAddressRange.restype = c_char_p
lib.mdAddrGetParsedPreDirection.argtypes = [c_void_p]
lib.mdAddrGetParsedPreDirection.restype = c_char_p
lib.mdAddrGetParsedStreetName.argtypes = [c_void_p]
lib.mdAddrGetParsedStreetName.restype = c_char_p
lib.mdAddrGetParsedSuffix.argtypes = [c_void_p]
lib.mdAddrGetParsedSuffix.restype = c_char_p
lib.mdAddrGetParsedPostDirection.argtypes = [c_void_p]
lib.mdAddrGetParsedPostDirection.restype = c_char_p
lib.mdAddrGetParsedSuiteName.argtypes = [c_void_p]
lib.mdAddrGetParsedSuiteName.restype = c_char_p
lib.mdAddrGetParsedSuiteRange.argtypes = [c_void_p]
lib.mdAddrGetParsedSuiteRange.restype = c_char_p
lib.mdAddrGetParsedPrivateMailboxName.argtypes = [c_void_p]
lib.mdAddrGetParsedPrivateMailboxName.restype = c_char_p
lib.mdAddrGetParsedPrivateMailboxNumber.argtypes = [c_void_p]
lib.mdAddrGetParsedPrivateMailboxNumber.restype = c_char_p
lib.mdAddrGetParsedGarbage.argtypes = [c_void_p]
lib.mdAddrGetParsedGarbage.restype = c_char_p
lib.mdAddrGetParsedRouteService.argtypes = [c_void_p]
lib.mdAddrGetParsedRouteService.restype = c_char_p
lib.mdAddrGetParsedLockBox.argtypes = [c_void_p]
lib.mdAddrGetParsedLockBox.restype = c_char_p
lib.mdAddrGetParsedDeliveryInstallation.argtypes = [c_void_p]
lib.mdAddrGetParsedDeliveryInstallation.restype = c_char_p
lib.mdAddrSetReserved.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdAddrSetReserved.restype = None
lib.mdAddrGetReserved.argtypes = [c_void_p, c_char_p]
lib.mdAddrGetReserved.restype = c_char_p

lib.mdParseCreate.argtypes = []
lib.mdParseCreate.restype = c_void_p
lib.mdParseDestroy.argtypes = [c_void_p]
lib.mdParseDestroy.restype = None
lib.mdParseInitialize.argtypes = [c_void_p, c_char_p]
lib.mdParseInitialize.restype = c_int
lib.mdParseGetBuildNumber.argtypes = [c_void_p]
lib.mdParseGetBuildNumber.restype = c_char_p
lib.mdParseParse.argtypes = [c_void_p, c_char_p]
lib.mdParseParse.restype = None
lib.mdParseParseCanadian.argtypes = [c_void_p, c_char_p]
lib.mdParseParseCanadian.restype = None
lib.mdParseParseNext.argtypes = [c_void_p]
lib.mdParseParseNext.restype = c_bool
lib.mdParseLastLineParse.argtypes = [c_void_p, c_char_p]
lib.mdParseLastLineParse.restype = None
lib.mdParseGetZip.argtypes = [c_void_p]
lib.mdParseGetZip.restype = c_char_p
lib.mdParseGetPlus4.argtypes = [c_void_p]
lib.mdParseGetPlus4.restype = c_char_p
lib.mdParseGetCity.argtypes = [c_void_p]
lib.mdParseGetCity.restype = c_char_p
lib.mdParseGetState.argtypes = [c_void_p]
lib.mdParseGetState.restype = c_char_p
lib.mdParseGetStreetName.argtypes = [c_void_p]
lib.mdParseGetStreetName.restype = c_char_p
lib.mdParseGetRange.argtypes = [c_void_p]
lib.mdParseGetRange.restype = c_char_p
lib.mdParseGetPreDirection.argtypes = [c_void_p]
lib.mdParseGetPreDirection.restype = c_char_p
lib.mdParseGetPostDirection.argtypes = [c_void_p]
lib.mdParseGetPostDirection.restype = c_char_p
lib.mdParseGetSuffix.argtypes = [c_void_p]
lib.mdParseGetSuffix.restype = c_char_p
lib.mdParseGetSuiteName.argtypes = [c_void_p]
lib.mdParseGetSuiteName.restype = c_char_p
lib.mdParseGetSuiteNumber.argtypes = [c_void_p]
lib.mdParseGetSuiteNumber.restype = c_char_p
lib.mdParseGetPrivateMailboxNumber.argtypes = [c_void_p]
lib.mdParseGetPrivateMailboxNumber.restype = c_char_p
lib.mdParseGetPrivateMailboxName.argtypes = [c_void_p]
lib.mdParseGetPrivateMailboxName.restype = c_char_p
lib.mdParseGetGarbage.argtypes = [c_void_p]
lib.mdParseGetGarbage.restype = c_char_p
lib.mdParseGetRouteService.argtypes = [c_void_p]
lib.mdParseGetRouteService.restype = c_char_p
lib.mdParseGetLockBox.argtypes = [c_void_p]
lib.mdParseGetLockBox.restype = c_char_p
lib.mdParseGetDeliveryInstallation.argtypes = [c_void_p]
lib.mdParseGetDeliveryInstallation.restype = c_char_p
if os.environ['DQS_VERSION'] >= 'dqs.202306':
  # This errors prior to dqs.202306.
  #   AttributeError: /melissa_data/dqs.202305/address/linux/gcc48_64bit/libmdAddr.so: undefined symbol:
  #   mdParseParseRule. Did you mean: 'mdParseParse'?
  lib.mdParseParseRule.argtypes = [c_void_p]
  lib.mdParseParseRule.restype = c_int

lib.mdStreetCreate.argtypes = []
lib.mdStreetCreate.restype = c_void_p
lib.mdStreetDestroy.argtypes = [c_void_p]
lib.mdStreetDestroy.restype = None
lib.mdStreetInitialize.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p]
lib.mdStreetInitialize.restype = c_int
lib.mdStreetGetInitializeErrorString.argtypes = [c_void_p]
lib.mdStreetGetInitializeErrorString.restype = c_char_p
lib.mdStreetGetDatabaseDate.argtypes = [c_void_p]
lib.mdStreetGetDatabaseDate.restype = c_char_p
lib.mdStreetGetBuildNumber.argtypes = [c_void_p]
lib.mdStreetGetBuildNumber.restype = c_char_p
lib.mdStreetSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdStreetSetLicenseString.restype = c_bool
lib.mdStreetGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdStreetGetLicenseExpirationDate.restype = c_char_p
lib.mdStreetFindStreet.argtypes = [c_void_p, c_char_p, c_char_p, c_bool]
lib.mdStreetFindStreet.restype = c_bool
lib.mdStreetFindStreetNext.argtypes = [c_void_p]
lib.mdStreetFindStreetNext.restype = c_bool
lib.mdStreetIsAddressInRange.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p]
lib.mdStreetIsAddressInRange.restype = c_bool
lib.mdStreetIsAddressInRange2.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p, c_char_p]
lib.mdStreetIsAddressInRange2.restype = c_bool
lib.mdStreetGetAutoCompletion.argtypes = [c_void_p, c_char_p, c_char_p, c_int, c_bool]
lib.mdStreetGetAutoCompletion.restype = c_char_p
lib.mdStreetResetAutoCompletion.argtypes = [c_void_p]
lib.mdStreetResetAutoCompletion.restype = None
lib.mdStreetGetBaseAlternateIndicator.argtypes = [c_void_p]
lib.mdStreetGetBaseAlternateIndicator.restype = c_char_p
lib.mdStreetGetLACSIndicator.argtypes = [c_void_p]
lib.mdStreetGetLACSIndicator.restype = c_char_p
lib.mdStreetGetUrbanizationCode.argtypes = [c_void_p]
lib.mdStreetGetUrbanizationCode.restype = c_char_p
lib.mdStreetGetUrbanizationName.argtypes = [c_void_p]
lib.mdStreetGetUrbanizationName.restype = c_char_p
lib.mdStreetGetLastLineNumber.argtypes = [c_void_p]
lib.mdStreetGetLastLineNumber.restype = c_char_p
lib.mdStreetGetAddressType.argtypes = [c_void_p]
lib.mdStreetGetAddressType.restype = c_char_p
lib.mdStreetGetCongressionalDistrict.argtypes = [c_void_p]
lib.mdStreetGetCongressionalDistrict.restype = c_char_p
lib.mdStreetGetCountyFips.argtypes = [c_void_p]
lib.mdStreetGetCountyFips.restype = c_char_p
lib.mdStreetGetCompany.argtypes = [c_void_p]
lib.mdStreetGetCompany.restype = c_char_p
lib.mdStreetGetCarrierRoute.argtypes = [c_void_p]
lib.mdStreetGetCarrierRoute.restype = c_char_p
lib.mdStreetGetZip.argtypes = [c_void_p]
lib.mdStreetGetZip.restype = c_char_p
lib.mdStreetGetDeliveryInstallation.argtypes = [c_void_p]
lib.mdStreetGetDeliveryInstallation.restype = c_char_p
lib.mdStreetGetPlus4High.argtypes = [c_void_p]
lib.mdStreetGetPlus4High.restype = c_char_p
lib.mdStreetGetPlus4Low.argtypes = [c_void_p]
lib.mdStreetGetPlus4Low.restype = c_char_p
lib.mdStreetGetSuiteRangeOddEven.argtypes = [c_void_p]
lib.mdStreetGetSuiteRangeOddEven.restype = c_char_p
lib.mdStreetGetSuiteRangeHigh.argtypes = [c_void_p]
lib.mdStreetGetSuiteRangeHigh.restype = c_char_p
lib.mdStreetGetSuiteRangeLow.argtypes = [c_void_p]
lib.mdStreetGetSuiteRangeLow.restype = c_char_p
lib.mdStreetGetSuiteName.argtypes = [c_void_p]
lib.mdStreetGetSuiteName.restype = c_char_p
lib.mdStreetGetPostDirection.argtypes = [c_void_p]
lib.mdStreetGetPostDirection.restype = c_char_p
lib.mdStreetGetSuffix.argtypes = [c_void_p]
lib.mdStreetGetSuffix.restype = c_char_p
lib.mdStreetGetStreetName.argtypes = [c_void_p]
lib.mdStreetGetStreetName.restype = c_char_p
lib.mdStreetGetPreDirection.argtypes = [c_void_p]
lib.mdStreetGetPreDirection.restype = c_char_p
lib.mdStreetGetPrimaryRangeOddEven.argtypes = [c_void_p]
lib.mdStreetGetPrimaryRangeOddEven.restype = c_char_p
lib.mdStreetGetPrimaryRangeHigh.argtypes = [c_void_p]
lib.mdStreetGetPrimaryRangeHigh.restype = c_char_p
lib.mdStreetGetPrimaryRangeLow.argtypes = [c_void_p]
lib.mdStreetGetPrimaryRangeLow.restype = c_char_p

lib.mdZipCreate.argtypes = []
lib.mdZipCreate.restype = c_void_p
lib.mdZipDestroy.argtypes = [c_void_p]
lib.mdZipDestroy.restype = None
lib.mdZipInitialize.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p]
lib.mdZipInitialize.restype = c_int
lib.mdZipGetInitializeErrorString.argtypes = [c_void_p]
lib.mdZipGetInitializeErrorString.restype = c_char_p
lib.mdZipGetDatabaseDate.argtypes = [c_void_p]
lib.mdZipGetDatabaseDate.restype = c_char_p
lib.mdZipGetBuildNumber.argtypes = [c_void_p]
lib.mdZipGetBuildNumber.restype = c_char_p
lib.mdZipSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdZipSetLicenseString.restype = c_bool
lib.mdZipGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdZipGetLicenseExpirationDate.restype = c_char_p
lib.mdZipFindZip.argtypes = [c_void_p, c_char_p, c_bool]
lib.mdZipFindZip.restype = c_bool
lib.mdZipFindZipNext.argtypes = [c_void_p]
lib.mdZipFindZipNext.restype = c_bool
lib.mdZipFindZipInCity.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdZipFindZipInCity.restype = c_bool
lib.mdZipFindZipInCityNext.argtypes = [c_void_p]
lib.mdZipFindZipInCityNext.restype = c_bool
lib.mdZipFindCityInState.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdZipFindCityInState.restype = c_bool
lib.mdZipFindCityInStateNext.argtypes = [c_void_p]
lib.mdZipFindCityInStateNext.restype = c_bool
lib.mdZipComputeDistance.argtypes = [c_void_p, c_double, c_double, c_double, c_double]
lib.mdZipComputeDistance.restype = c_double
lib.mdZipComputeBearing.argtypes = [c_void_p, c_double, c_double, c_double, c_double]
lib.mdZipComputeBearing.restype = c_double
lib.mdZipGetCountyNameFromFips.argtypes = [c_void_p, c_char_p]
lib.mdZipGetCountyNameFromFips.restype = c_char_p
lib.mdZipGetSCFArea.argtypes = [c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p]
lib.mdZipGetSCFArea.restype = c_int
lib.mdZipGetZip.argtypes = [c_void_p]
lib.mdZipGetZip.restype = c_char_p
lib.mdZipGetCity.argtypes = [c_void_p]
lib.mdZipGetCity.restype = c_char_p
lib.mdZipGetCityAbbreviation.argtypes = [c_void_p]
lib.mdZipGetCityAbbreviation.restype = c_char_p
lib.mdZipGetState.argtypes = [c_void_p]
lib.mdZipGetState.restype = c_char_p
lib.mdZipGetZipType.argtypes = [c_void_p]
lib.mdZipGetZipType.restype = c_char_p
lib.mdZipGetCountyName.argtypes = [c_void_p]
lib.mdZipGetCountyName.restype = c_char_p
lib.mdZipGetCountyFips.argtypes = [c_void_p]
lib.mdZipGetCountyFips.restype = c_char_p
lib.mdZipGetAreaCode.argtypes = [c_void_p]
lib.mdZipGetAreaCode.restype = c_char_p
lib.mdZipGetLongitude.argtypes = [c_void_p]
lib.mdZipGetLongitude.restype = c_char_p
lib.mdZipGetLatitude.argtypes = [c_void_p]
lib.mdZipGetLatitude.restype = c_char_p
lib.mdZipGetTimeZone.argtypes = [c_void_p]
lib.mdZipGetTimeZone.restype = c_char_p
lib.mdZipGetTimeZoneCode.argtypes = [c_void_p]
lib.mdZipGetTimeZoneCode.restype = c_char_p
lib.mdZipGetMsa.argtypes = [c_void_p]
lib.mdZipGetMsa.restype = c_char_p
lib.mdZipGetPmsa.argtypes = [c_void_p]
lib.mdZipGetPmsa.restype = c_char_p
lib.mdZipGetFacilityCode.argtypes = [c_void_p]
lib.mdZipGetFacilityCode.restype = c_char_p
lib.mdZipGetLastLineIndicator.argtypes = [c_void_p]
lib.mdZipGetLastLineIndicator.restype = c_char_p
lib.mdZipGetLastLineNumber.argtypes = [c_void_p]
lib.mdZipGetLastLineNumber.restype = c_char_p
lib.mdZipGetPreferredLastLineNumber.argtypes = [c_void_p]
lib.mdZipGetPreferredLastLineNumber.restype = c_char_p
lib.mdZipGetAutomation.argtypes = [c_void_p]
lib.mdZipGetAutomation.restype = c_char_p
lib.mdZipGetFinanceNumber.argtypes = [c_void_p]
lib.mdZipGetFinanceNumber.restype = c_char_p

# mdAddr Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorOther = 1
	ErrorOutOfMemory = 2
	ErrorRequiredFileNotFound = 3
	ErrorFoundOldFile = 4
	ErrorDatabaseExpired = 5
	ErrorLicenseExpired = 6

class AccessType(Enum):
	Local = 0
	Remote = 1

class DiacriticsMode(Enum):
	Auto = 0
	On = 1
	Off = 2

class StandardizeMode(Enum):
	ShortFormat = 0
	LongFormat = 1
	AutoFormat = 2

class SuiteParseMode(Enum):
	ParseSuite = 0
	CombineSuite = 1

class AliasPreserveMode(Enum):
	ConvertAlias = 0
	PreserveAlias = 1

class AutoCompletionMode(Enum):
	AutoCompleteSingleSuite = 0
	AutoCompleteRangedSuite = 1
	AutoCompletePlaceHolderSuite = 2
	AutoCompleteNoSuite = 3

class ResultCdDescOpt(Enum):
	ResultCodeDescriptionLong = 0
	ResultCodeDescriptionShort = 1

class MailboxLookupMode(Enum):
	MailboxNone = 0
	MailboxExpress = 1
	MailboxPremium = 2

class mdAddr(object):
	def __init__(self, encoding, errors):
		self.encoding = encoding
		self.errors = errors
		self.I = lib.mdAddrCreate()

	def __del__(self):
		lib.mdAddrDestroy(self.I)

	def Initialize(self, p1, p2, p3):
		return ProgramStatus(lib.mdAddrInitialize(self.I, p1.encode(self.encoding, errors=self.errors), p2.encode(self.encoding, errors=self.errors), p3.encode(self.encoding, errors=self.errors)))

	def InitializeDataFiles(self):
		return ProgramStatus(lib.mdAddrInitializeDataFiles(self.I))

	def GetInitializeErrorString(self):
		return lib.mdAddrGetInitializeErrorString(self.I).decode(self.encoding)

	def SetLicenseString(self, p1):
		return lib.mdAddrSetLicenseString(self.I, p1.encode(self.encoding, errors=self.errors))

	def GetBuildNumber(self):
		return lib.mdAddrGetBuildNumber(self.I).decode(self.encoding)

	def GetDatabaseDate(self):
		return lib.mdAddrGetDatabaseDate(self.I).decode(self.encoding)

	def GetExpirationDate(self):
		return lib.mdAddrGetExpirationDate(self.I).decode(self.encoding)

	def GetLicenseExpirationDate(self):
		return lib.mdAddrGetLicenseExpirationDate(self.I).decode(self.encoding)

	def GetCanadianDatabaseDate(self):
		return lib.mdAddrGetCanadianDatabaseDate(self.I).decode(self.encoding)

	def GetCanadianExpirationDate(self):
		return lib.mdAddrGetCanadianExpirationDate(self.I).decode(self.encoding)

	def SetPathToUSFiles(self, p1):
		lib.mdAddrSetPathToUSFiles(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPathToCanadaFiles(self, p1):
		lib.mdAddrSetPathToCanadaFiles(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPathToDPVDataFiles(self, p1):
		lib.mdAddrSetPathToDPVDataFiles(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPathToLACSLinkDataFiles(self, p1):
		lib.mdAddrSetPathToLACSLinkDataFiles(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPathToSuiteLinkDataFiles(self, p1):
		lib.mdAddrSetPathToSuiteLinkDataFiles(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPathToSuiteFinderDataFiles(self, p1):
		lib.mdAddrSetPathToSuiteFinderDataFiles(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPathToRBDIFiles(self, p1):
		lib.mdAddrSetPathToRBDIFiles(self.I, p1.encode(self.encoding, errors=self.errors))

	def GetRBDIDatabaseDate(self):
		return lib.mdAddrGetRBDIDatabaseDate(self.I).decode(self.encoding)

	def SetPathToAddrKeyDataFiles(self, p1):
		lib.mdAddrSetPathToAddrKeyDataFiles(self.I, p1.encode(self.encoding, errors=self.errors))

	def ClearProperties(self):
		lib.mdAddrClearProperties(self.I)

	def ResetDPV(self):
		lib.mdAddrResetDPV(self.I)

	def SetCASSEnable(self, p1):
		lib.mdAddrSetCASSEnable(self.I, p1)

	def SetUseUSPSPreferredCityNames(self, p1):
		lib.mdAddrSetUseUSPSPreferredCityNames(self.I, p1)

	def SetDiacritics(self, p1):
		lib.mdAddrSetDiacritics(self.I, DiacriticsMode(p1).value)

	def GetStatusCode(self):
		return lib.mdAddrGetStatusCode(self.I).decode(self.encoding)

	def GetErrorCode(self):
		return lib.mdAddrGetErrorCode(self.I).decode(self.encoding)

	def GetErrorString(self):
		return lib.mdAddrGetErrorString(self.I).decode(self.encoding)

	def GetResults(self):
		return lib.mdAddrGetResults(self.I).decode(self.encoding)

	def GetResultCodeDescription(self, resultCode, opt=0):
		return lib.mdAddrGetResultCodeDescription(self.I, resultCode.encode(self.encoding, errors=self.errors), ResultCdDescOpt(opt).value).decode(self.encoding)

	def SetPS3553_B1_ProcessorName(self, p1):
		lib.mdAddrSetPS3553_B1_ProcessorName(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPS3553_B4_ListName(self, p1):
		lib.mdAddrSetPS3553_B4_ListName(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPS3553_D3_Name(self, p1):
		lib.mdAddrSetPS3553_D3_Name(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPS3553_D3_Company(self, p1):
		lib.mdAddrSetPS3553_D3_Company(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPS3553_D3_Address(self, p1):
		lib.mdAddrSetPS3553_D3_Address(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPS3553_D3_City(self, p1):
		lib.mdAddrSetPS3553_D3_City(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPS3553_D3_State(self, p1):
		lib.mdAddrSetPS3553_D3_State(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPS3553_D3_ZIP(self, p1):
		lib.mdAddrSetPS3553_D3_ZIP(self.I, p1.encode(self.encoding, errors=self.errors))

	def GetFormPS3553(self):
		return lib.mdAddrGetFormPS3553(self.I).decode(self.encoding)

	def SaveFormPS3553(self, p1):
		return lib.mdAddrSaveFormPS3553(self.I, p1.encode(self.encoding, errors=self.errors))

	def ResetFormPS3553(self):
		lib.mdAddrResetFormPS3553(self.I)

	def ResetFormPS3553Counter(self):
		lib.mdAddrResetFormPS3553Counter(self.I)

	def SetStandardizationType(self, mode):
		lib.mdAddrSetStandardizationType(self.I, StandardizeMode(mode).value)

	def SetSuiteParseMode(self, mode):
		lib.mdAddrSetSuiteParseMode(self.I, SuiteParseMode(mode).value)

	def SetAliasMode(self, mode):
		lib.mdAddrSetAliasMode(self.I, AliasPreserveMode(mode).value)

	def GetFormSOA(self):
		return lib.mdAddrGetFormSOA(self.I).decode(self.encoding)

	def SaveFormSOA(self, p1):
		lib.mdAddrSaveFormSOA(self.I, p1.encode(self.encoding, errors=self.errors))

	def ResetFormSOA(self):
		lib.mdAddrResetFormSOA(self.I)

	def SetSOACustomerInfo(self, customerName, customerAddress):
		lib.mdAddrSetSOACustomerInfo(self.I, customerName.encode(self.encoding, errors=self.errors), customerAddress.encode(self.encoding, errors=self.errors))

	def SetSOACPCNumber(self, CPCNumber):
		lib.mdAddrSetSOACPCNumber(self.I, CPCNumber.encode(self.encoding, errors=self.errors))

	def GetSOACustomerInfo(self):
		return lib.mdAddrGetSOACustomerInfo(self.I).decode(self.encoding)

	def GetSOACPCNumber(self):
		return lib.mdAddrGetSOACPCNumber(self.I).decode(self.encoding)

	def GetSOATotalRecords(self):
		return lib.mdAddrGetSOATotalRecords(self.I)

	def GetSOAAAPercentage(self):
		return lib.mdAddrGetSOAAAPercentage(self.I)

	def GetSOAAAExpiryDate(self):
		return lib.mdAddrGetSOAAAExpiryDate(self.I).decode(self.encoding)

	def GetSOASoftwareInfo(self):
		return lib.mdAddrGetSOASoftwareInfo(self.I).decode(self.encoding)

	def GetSOAErrorString(self):
		return lib.mdAddrGetSOAErrorString(self.I).decode(self.encoding)

	def SetCompany(self, p1):
		lib.mdAddrSetCompany(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetLastName(self, p1):
		lib.mdAddrSetLastName(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetAddress(self, p1):
		lib.mdAddrSetAddress(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetAddress2(self, p1):
		lib.mdAddrSetAddress2(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetLastLine(self, p1):
		lib.mdAddrSetLastLine(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetSuite(self, p1):
		lib.mdAddrSetSuite(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetCity(self, p1):
		lib.mdAddrSetCity(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetState(self, p1):
		lib.mdAddrSetState(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetZip(self, p1):
		lib.mdAddrSetZip(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetPlus4(self, p1):
		lib.mdAddrSetPlus4(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetUrbanization(self, p1):
		lib.mdAddrSetUrbanization(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetParsedAddressRange(self, p1):
		lib.mdAddrSetParsedAddressRange(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetParsedPreDirection(self, p1):
		lib.mdAddrSetParsedPreDirection(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetParsedStreetName(self, p1):
		lib.mdAddrSetParsedStreetName(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetParsedSuffix(self, p1):
		lib.mdAddrSetParsedSuffix(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetParsedPostDirection(self, p1):
		lib.mdAddrSetParsedPostDirection(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetParsedSuiteName(self, p1):
		lib.mdAddrSetParsedSuiteName(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetParsedSuiteRange(self, p1):
		lib.mdAddrSetParsedSuiteRange(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetParsedRouteService(self, p1):
		lib.mdAddrSetParsedRouteService(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetParsedLockBox(self, p1):
		lib.mdAddrSetParsedLockBox(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetParsedDeliveryInstallation(self, p1):
		lib.mdAddrSetParsedDeliveryInstallation(self.I, p1.encode(self.encoding, errors=self.errors))

	def SetCountryCode(self, p1):
		lib.mdAddrSetCountryCode(self.I, p1.encode(self.encoding, errors=self.errors))

	def VerifyAddress(self):
		return lib.mdAddrVerifyAddress(self.I)

	def GetCompany(self):
		return lib.mdAddrGetCompany(self.I).decode(self.encoding)

	def GetLastName(self):
		return lib.mdAddrGetLastName(self.I).decode(self.encoding)

	def GetAddress(self):
		return lib.mdAddrGetAddress(self.I).decode(self.encoding)

	def GetAddress2(self):
		return lib.mdAddrGetAddress2(self.I).decode(self.encoding)

	def GetSuite(self):
		return lib.mdAddrGetSuite(self.I).decode(self.encoding)

	def GetCity(self):
		return lib.mdAddrGetCity(self.I).decode(self.encoding)

	def GetCityAbbreviation(self):
		return lib.mdAddrGetCityAbbreviation(self.I).decode(self.encoding)

	def GetState(self):
		return lib.mdAddrGetState(self.I).decode(self.encoding)

	def GetZip(self):
		return lib.mdAddrGetZip(self.I).decode(self.encoding)

	def GetPlus4(self):
		return lib.mdAddrGetPlus4(self.I).decode(self.encoding)

	def GetCarrierRoute(self):
		return lib.mdAddrGetCarrierRoute(self.I).decode(self.encoding)

	def GetDeliveryPointCode(self):
		return lib.mdAddrGetDeliveryPointCode(self.I).decode(self.encoding)

	def GetDeliveryPointCheckDigit(self):
		return lib.mdAddrGetDeliveryPointCheckDigit(self.I).decode(self.encoding)

	def GetCountyFips(self):
		return lib.mdAddrGetCountyFips(self.I).decode(self.encoding)

	def GetCountyName(self):
		return lib.mdAddrGetCountyName(self.I).decode(self.encoding)

	def GetAddressTypeCode(self):
		return lib.mdAddrGetAddressTypeCode(self.I).decode(self.encoding)

	def GetAddressTypeString(self):
		return lib.mdAddrGetAddressTypeString(self.I).decode(self.encoding)

	def GetUrbanization(self):
		return lib.mdAddrGetUrbanization(self.I).decode(self.encoding)

	def GetCongressionalDistrict(self):
		return lib.mdAddrGetCongressionalDistrict(self.I).decode(self.encoding)

	def GetLACS(self):
		return lib.mdAddrGetLACS(self.I).decode(self.encoding)

	def GetLACSLinkIndicator(self):
		return lib.mdAddrGetLACSLinkIndicator(self.I).decode(self.encoding)

	def GetPrivateMailbox(self):
		return lib.mdAddrGetPrivateMailbox(self.I).decode(self.encoding)

	def GetTimeZoneCode(self):
		return lib.mdAddrGetTimeZoneCode(self.I).decode(self.encoding)

	def GetTimeZone(self):
		return lib.mdAddrGetTimeZone(self.I).decode(self.encoding)

	def GetMsa(self):
		return lib.mdAddrGetMsa(self.I).decode(self.encoding)

	def GetPmsa(self):
		return lib.mdAddrGetPmsa(self.I).decode(self.encoding)

	def GetDefaultFlagIndicator(self):
		return lib.mdAddrGetDefaultFlagIndicator(self.I).decode(self.encoding)

	def GetSuiteStatus(self):
		return lib.mdAddrGetSuiteStatus(self.I).decode(self.encoding)

	def GetEWSFlag(self):
		return lib.mdAddrGetEWSFlag(self.I).decode(self.encoding)

	def GetCMRA(self):
		return lib.mdAddrGetCMRA(self.I).decode(self.encoding)

	def GetDsfVacant(self):
		return lib.mdAddrGetDsfVacant(self.I).decode(self.encoding)

	def GetCountryCode(self):
		return lib.mdAddrGetCountryCode(self.I).decode(self.encoding)

	def GetZipType(self):
		return lib.mdAddrGetZipType(self.I).decode(self.encoding)

	def GetFalseTable(self):
		return lib.mdAddrGetFalseTable(self.I).decode(self.encoding)

	def GetDPVFootnotes(self):
		return lib.mdAddrGetDPVFootnotes(self.I).decode(self.encoding)

	def GetLACSLinkReturnCode(self):
		return lib.mdAddrGetLACSLinkReturnCode(self.I).decode(self.encoding)

	def GetSuiteLinkReturnCode(self):
		return lib.mdAddrGetSuiteLinkReturnCode(self.I).decode(self.encoding)

	def GetRBDI(self):
		return lib.mdAddrGetRBDI(self.I).decode(self.encoding)

	def GetELotNumber(self):
		return lib.mdAddrGetELotNumber(self.I).decode(self.encoding)

	def GetELotOrder(self):
		return lib.mdAddrGetELotOrder(self.I).decode(self.encoding)

	def GetAddressKey(self):
		return lib.mdAddrGetAddressKey(self.I).decode(self.encoding)

	def GetMelissaAddressKey(self):
		return lib.mdAddrGetMelissaAddressKey(self.I).decode(self.encoding)

	def GetMelissaAddressKeyBase(self):
		return lib.mdAddrGetMelissaAddressKeyBase(self.I).decode(self.encoding)

	def GetOutputParameter(self, p1):
		return lib.mdAddrGetOutputParameter(self.I, p1.encode(self.encoding, errors=self.errors)).decode(self.encoding)

	def SetInputParameter(self, p1, p2):
		return lib.mdAddrSetInputParameter(self.I, p1.encode(self.encoding, errors=self.errors), p2.encode(self.encoding, errors=self.errors))

	def FindSuggestion(self):
		return lib.mdAddrFindSuggestion(self.I)

	def FindSuggestionNext(self):
		return lib.mdAddrFindSuggestionNext(self.I)

	def GetDsfNoStats(self):
		return lib.mdAddrGetDsfNoStats(self.I).decode(self.encoding)

	def GetDsfDNA(self):
		return lib.mdAddrGetDsfDNA(self.I).decode(self.encoding)

	def GetPS3553_B6_TotalRecords(self):
		return lib.mdAddrGetPS3553_B6_TotalRecords(self.I)

	def GetPS3553_C1a_ZIP4Coded(self):
		return lib.mdAddrGetPS3553_C1a_ZIP4Coded(self.I)

	def GetPS3553_C1c_DPBCAssigned(self):
		return lib.mdAddrGetPS3553_C1c_DPBCAssigned(self.I)

	def GetPS3553_C1d_FiveDigitCoded(self):
		return lib.mdAddrGetPS3553_C1d_FiveDigitCoded(self.I)

	def GetPS3553_C1e_CRRTCoded(self):
		return lib.mdAddrGetPS3553_C1e_CRRTCoded(self.I)

	def GetPS3553_C1f_eLOTAssigned(self):
		return lib.mdAddrGetPS3553_C1f_eLOTAssigned(self.I)

	def GetPS3553_E_HighRiseDefault(self):
		return lib.mdAddrGetPS3553_E_HighRiseDefault(self.I)

	def GetPS3553_E_HighRiseExact(self):
		return lib.mdAddrGetPS3553_E_HighRiseExact(self.I)

	def GetPS3553_E_RuralRouteDefault(self):
		return lib.mdAddrGetPS3553_E_RuralRouteDefault(self.I)

	def GetPS3553_E_RuralRouteExact(self):
		return lib.mdAddrGetPS3553_E_RuralRouteExact(self.I)

	def GetZip4HRDefault(self):
		return lib.mdAddrGetZip4HRDefault(self.I)

	def GetZip4HRExact(self):
		return lib.mdAddrGetZip4HRExact(self.I)

	def GetZip4RRDefault(self):
		return lib.mdAddrGetZip4RRDefault(self.I)

	def GetZip4RRExact(self):
		return lib.mdAddrGetZip4RRExact(self.I)

	def GetPS3553_E_LACSCount(self):
		return lib.mdAddrGetPS3553_E_LACSCount(self.I)

	def GetPS3553_E_EWSCount(self):
		return lib.mdAddrGetPS3553_E_EWSCount(self.I)

	def GetPS3553_E_DPVCount(self):
		return lib.mdAddrGetPS3553_E_DPVCount(self.I)

	def GetPS3553_X_POBoxCount(self):
		return lib.mdAddrGetPS3553_X_POBoxCount(self.I)

	def GetPS3553_X_HCExactCount(self):
		return lib.mdAddrGetPS3553_X_HCExactCount(self.I)

	def GetPS3553_X_FirmCount(self):
		return lib.mdAddrGetPS3553_X_FirmCount(self.I)

	def GetPS3553_X_GenDeliveryCount(self):
		return lib.mdAddrGetPS3553_X_GenDeliveryCount(self.I)

	def GetPS3553_X_MilitaryZipCount(self):
		return lib.mdAddrGetPS3553_X_MilitaryZipCount(self.I)

	def GetPS3553_X_NonDeliveryCount(self):
		return lib.mdAddrGetPS3553_X_NonDeliveryCount(self.I)

	def GetPS3553_X_StreetCount(self):
		return lib.mdAddrGetPS3553_X_StreetCount(self.I)

	def GetPS3553_X_HCDefaultCount(self):
		return lib.mdAddrGetPS3553_X_HCDefaultCount(self.I)

	def GetPS3553_X_OtherCount(self):
		return lib.mdAddrGetPS3553_X_OtherCount(self.I)

	def GetPS3553_X_LacsLinkCodeACount(self):
		return lib.mdAddrGetPS3553_X_LacsLinkCodeACount(self.I)

	def GetPS3553_X_LacsLinkCode00Count(self):
		return lib.mdAddrGetPS3553_X_LacsLinkCode00Count(self.I)

	def GetPS3553_X_LacsLinkCode14Count(self):
		return lib.mdAddrGetPS3553_X_LacsLinkCode14Count(self.I)

	def GetPS3553_X_LacsLinkCode92Count(self):
		return lib.mdAddrGetPS3553_X_LacsLinkCode92Count(self.I)

	def GetPS3553_X_LacsLinkCode09Count(self):
		return lib.mdAddrGetPS3553_X_LacsLinkCode09Count(self.I)

	def GetPS3553_X_SuiteLinkCodeACount(self):
		return lib.mdAddrGetPS3553_X_SuiteLinkCodeACount(self.I)

	def GetPS3553_X_SuiteLinkCode00Count(self):
		return lib.mdAddrGetPS3553_X_SuiteLinkCode00Count(self.I)

	def GetParsedAddressRange(self):
		return lib.mdAddrGetParsedAddressRange(self.I).decode(self.encoding)

	def GetParsedPreDirection(self):
		return lib.mdAddrGetParsedPreDirection(self.I).decode(self.encoding)

	def GetParsedStreetName(self):
		return lib.mdAddrGetParsedStreetName(self.I).decode(self.encoding)

	def GetParsedSuffix(self):
		return lib.mdAddrGetParsedSuffix(self.I).decode(self.encoding)

	def GetParsedPostDirection(self):
		return lib.mdAddrGetParsedPostDirection(self.I).decode(self.encoding)

	def GetParsedSuiteName(self):
		return lib.mdAddrGetParsedSuiteName(self.I).decode(self.encoding)

	def GetParsedSuiteRange(self):
		return lib.mdAddrGetParsedSuiteRange(self.I).decode(self.encoding)

	def GetParsedPrivateMailboxName(self):
		return lib.mdAddrGetParsedPrivateMailboxName(self.I).decode(self.encoding)

	def GetParsedPrivateMailboxNumber(self):
		return lib.mdAddrGetParsedPrivateMailboxNumber(self.I).decode(self.encoding)

	def GetParsedGarbage(self):
		return lib.mdAddrGetParsedGarbage(self.I).decode(self.encoding)

	def GetParsedRouteService(self):
		return lib.mdAddrGetParsedRouteService(self.I).decode(self.encoding)

	def GetParsedLockBox(self):
		return lib.mdAddrGetParsedLockBox(self.I).decode(self.encoding)

	def GetParsedDeliveryInstallation(self):
		return lib.mdAddrGetParsedDeliveryInstallation(self.I).decode(self.encoding)

	def SetReserved(self, p1, p2):
		lib.mdAddrSetReserved(self.I, p1.encode(self.encoding, errors=self.errors), p2.encode(self.encoding, errors=self.errors))

	def GetReserved(self, p1):
		return lib.mdAddrGetReserved(self.I, p1.encode(self.encoding, errors=self.errors)).decode(self.encoding)

# mdParse Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorOther = 1
	ErrorOutOfMemory = 2
	ErrorRequiredFileNotFound = 3
	ErrorFoundOldFile = 4
	ErrorDatabaseExpired = 5
	ErrorLicenseExpired = 6

class AccessType(Enum):
	Local = 0
	Remote = 1

class DiacriticsMode(Enum):
	Auto = 0
	On = 1
	Off = 2

class StandardizeMode(Enum):
	ShortFormat = 0
	LongFormat = 1
	AutoFormat = 2

class SuiteParseMode(Enum):
	ParseSuite = 0
	CombineSuite = 1

class AliasPreserveMode(Enum):
	ConvertAlias = 0
	PreserveAlias = 1

class AutoCompletionMode(Enum):
	AutoCompleteSingleSuite = 0
	AutoCompleteRangedSuite = 1
	AutoCompletePlaceHolderSuite = 2
	AutoCompleteNoSuite = 3

class ResultCdDescOpt(Enum):
	ResultCodeDescriptionLong = 0
	ResultCodeDescriptionShort = 1

class MailboxLookupMode(Enum):
	MailboxNone = 0
	MailboxExpress = 1
	MailboxPremium = 2

class mdParse(object):
	def __init__(self, encoding, errors):
		self.encoding = encoding
		self.errors = errors
		self.I = lib.mdParseCreate()

	def __del__(self):
		lib.mdParseDestroy(self.I)

	def Initialize(self, p1):
		return ProgramStatus(lib.mdParseInitialize(self.I, p1.encode(self.encoding, errors=self.errors)))

	def GetBuildNumber(self):
		return lib.mdParseGetBuildNumber(self.I).decode(self.encoding)

	def Parse(self, p1):
		lib.mdParseParse(self.I, p1.encode(self.encoding, errors=self.errors))

	def ParseCanadian(self, p1):
		lib.mdParseParseCanadian(self.I, p1.encode(self.encoding, errors=self.errors))

	def ParseNext(self):
		return lib.mdParseParseNext(self.I)

	def LastLineParse(self, p1):
		lib.mdParseLastLineParse(self.I, p1.encode(self.encoding, errors=self.errors))

	def GetZip(self):
		return lib.mdParseGetZip(self.I).decode(self.encoding)

	def GetPlus4(self):
		return lib.mdParseGetPlus4(self.I).decode(self.encoding)

	def GetCity(self):
		return lib.mdParseGetCity(self.I).decode(self.encoding)

	def GetState(self):
		return lib.mdParseGetState(self.I).decode(self.encoding)

	def GetStreetName(self):
		return lib.mdParseGetStreetName(self.I).decode(self.encoding)

	def GetRange(self):
		return lib.mdParseGetRange(self.I).decode(self.encoding)

	def GetPreDirection(self):
		return lib.mdParseGetPreDirection(self.I).decode(self.encoding)

	def GetPostDirection(self):
		return lib.mdParseGetPostDirection(self.I).decode(self.encoding)

	def GetSuffix(self):
		return lib.mdParseGetSuffix(self.I).decode(self.encoding)

	def GetSuiteName(self):
		return lib.mdParseGetSuiteName(self.I).decode(self.encoding)

	def GetSuiteNumber(self):
		return lib.mdParseGetSuiteNumber(self.I).decode(self.encoding)

	def GetPrivateMailboxNumber(self):
		return lib.mdParseGetPrivateMailboxNumber(self.I).decode(self.encoding)

	def GetPrivateMailboxName(self):
		return lib.mdParseGetPrivateMailboxName(self.I).decode(self.encoding)

	def GetGarbage(self):
		return lib.mdParseGetGarbage(self.I).decode(self.encoding)

	def GetRouteService(self):
		return lib.mdParseGetRouteService(self.I).decode(self.encoding)

	def GetLockBox(self):
		return lib.mdParseGetLockBox(self.I).decode(self.encoding)

	def GetDeliveryInstallation(self):
		return lib.mdParseGetDeliveryInstallation(self.I).decode(self.encoding)

	def ParseRule(self):
		return lib.mdParseParseRule(self.I)

# mdStreet Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorOther = 1
	ErrorOutOfMemory = 2
	ErrorRequiredFileNotFound = 3
	ErrorFoundOldFile = 4
	ErrorDatabaseExpired = 5
	ErrorLicenseExpired = 6

class AccessType(Enum):
	Local = 0
	Remote = 1

class DiacriticsMode(Enum):
	Auto = 0
	On = 1
	Off = 2

class StandardizeMode(Enum):
	ShortFormat = 0
	LongFormat = 1
	AutoFormat = 2

class SuiteParseMode(Enum):
	ParseSuite = 0
	CombineSuite = 1

class AliasPreserveMode(Enum):
	ConvertAlias = 0
	PreserveAlias = 1

class AutoCompletionMode(Enum):
	AutoCompleteSingleSuite = 0
	AutoCompleteRangedSuite = 1
	AutoCompletePlaceHolderSuite = 2
	AutoCompleteNoSuite = 3

class ResultCdDescOpt(Enum):
	ResultCodeDescriptionLong = 0
	ResultCodeDescriptionShort = 1

class MailboxLookupMode(Enum):
	MailboxNone = 0
	MailboxExpress = 1
	MailboxPremium = 2

class mdStreet(object):
	def __init__(self, encoding, errors):
		self.encoding = encoding
		self.errors = errors
		self.I = lib.mdStreetCreate()

	def __del__(self):
		lib.mdStreetDestroy(self.I)

	def Initialize(self, p1, p2, p3):
		return ProgramStatus(lib.mdStreetInitialize(self.I, p1.encode(self.encoding, errors=self.errors), p2.encode(self.encoding, errors=self.errors), p3.encode(self.encoding, errors=self.errors)))

	def GetInitializeErrorString(self):
		return lib.mdStreetGetInitializeErrorString(self.I).decode(self.encoding)

	def GetDatabaseDate(self):
		return lib.mdStreetGetDatabaseDate(self.I).decode(self.encoding)

	def GetBuildNumber(self):
		return lib.mdStreetGetBuildNumber(self.I).decode(self.encoding)

	def SetLicenseString(self, p1):
		return lib.mdStreetSetLicenseString(self.I, p1.encode(self.encoding, errors=self.errors))

	def GetLicenseExpirationDate(self):
		return lib.mdStreetGetLicenseExpirationDate(self.I).decode(self.encoding)

	def FindStreet(self, p1, p2, p3):
		return lib.mdStreetFindStreet(self.I, p1.encode(self.encoding, errors=self.errors), p2.encode(self.encoding, errors=self.errors), p3)

	def FindStreetNext(self):
		return lib.mdStreetFindStreetNext(self.I)

	def IsAddressInRange(self, p1, p2, p3):
		return lib.mdStreetIsAddressInRange(self.I, p1.encode(self.encoding, errors=self.errors), p2.encode(self.encoding, errors=self.errors), p3.encode(self.encoding, errors=self.errors))

	def IsAddressInRange2(self, p1, p2, p3, p4):
		return lib.mdStreetIsAddressInRange2(self.I, p1.encode(self.encoding, errors=self.errors), p2.encode(self.encoding, errors=self.errors), p3.encode(self.encoding, errors=self.errors), p4.encode(self.encoding, errors=self.errors))

	def GetAutoCompletion(self, p1, p2, p3, p4):
		return lib.mdStreetGetAutoCompletion(self.I, p1.encode(self.encoding, errors=self.errors), p2.encode(self.encoding, errors=self.errors), AutoCompletionMode(p3).value, p4).decode(self.encoding)

	def ResetAutoCompletion(self):
		lib.mdStreetResetAutoCompletion(self.I)

	def GetBaseAlternateIndicator(self):
		return lib.mdStreetGetBaseAlternateIndicator(self.I).decode(self.encoding)

	def GetLACSIndicator(self):
		return lib.mdStreetGetLACSIndicator(self.I).decode(self.encoding)

	def GetUrbanizationCode(self):
		return lib.mdStreetGetUrbanizationCode(self.I).decode(self.encoding)

	def GetUrbanizationName(self):
		return lib.mdStreetGetUrbanizationName(self.I).decode(self.encoding)

	def GetLastLineNumber(self):
		return lib.mdStreetGetLastLineNumber(self.I).decode(self.encoding)

	def GetAddressType(self):
		return lib.mdStreetGetAddressType(self.I).decode(self.encoding)

	def GetCongressionalDistrict(self):
		return lib.mdStreetGetCongressionalDistrict(self.I).decode(self.encoding)

	def GetCountyFips(self):
		return lib.mdStreetGetCountyFips(self.I).decode(self.encoding)

	def GetCompany(self):
		return lib.mdStreetGetCompany(self.I).decode(self.encoding)

	def GetCarrierRoute(self):
		return lib.mdStreetGetCarrierRoute(self.I).decode(self.encoding)

	def GetZip(self):
		return lib.mdStreetGetZip(self.I).decode(self.encoding)

	def GetDeliveryInstallation(self):
		return lib.mdStreetGetDeliveryInstallation(self.I).decode(self.encoding)

	def GetPlus4High(self):
		return lib.mdStreetGetPlus4High(self.I).decode(self.encoding)

	def GetPlus4Low(self):
		return lib.mdStreetGetPlus4Low(self.I).decode(self.encoding)

	def GetSuiteRangeOddEven(self):
		return lib.mdStreetGetSuiteRangeOddEven(self.I).decode(self.encoding)

	def GetSuiteRangeHigh(self):
		return lib.mdStreetGetSuiteRangeHigh(self.I).decode(self.encoding)

	def GetSuiteRangeLow(self):
		return lib.mdStreetGetSuiteRangeLow(self.I).decode(self.encoding)

	def GetSuiteName(self):
		return lib.mdStreetGetSuiteName(self.I).decode(self.encoding)

	def GetPostDirection(self):
		return lib.mdStreetGetPostDirection(self.I).decode(self.encoding)

	def GetSuffix(self):
		return lib.mdStreetGetSuffix(self.I).decode(self.encoding)

	def GetStreetName(self):
		return lib.mdStreetGetStreetName(self.I).decode(self.encoding)

	def GetPreDirection(self):
		return lib.mdStreetGetPreDirection(self.I).decode(self.encoding)

	def GetPrimaryRangeOddEven(self):
		return lib.mdStreetGetPrimaryRangeOddEven(self.I).decode(self.encoding)

	def GetPrimaryRangeHigh(self):
		return lib.mdStreetGetPrimaryRangeHigh(self.I).decode(self.encoding)

	def GetPrimaryRangeLow(self):
		return lib.mdStreetGetPrimaryRangeLow(self.I).decode(self.encoding)

# mdZip Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorOther = 1
	ErrorOutOfMemory = 2
	ErrorRequiredFileNotFound = 3
	ErrorFoundOldFile = 4
	ErrorDatabaseExpired = 5
	ErrorLicenseExpired = 6

class AccessType(Enum):
	Local = 0
	Remote = 1

class DiacriticsMode(Enum):
	Auto = 0
	On = 1
	Off = 2

class StandardizeMode(Enum):
	ShortFormat = 0
	LongFormat = 1
	AutoFormat = 2

class SuiteParseMode(Enum):
	ParseSuite = 0
	CombineSuite = 1

class AliasPreserveMode(Enum):
	ConvertAlias = 0
	PreserveAlias = 1

class AutoCompletionMode(Enum):
	AutoCompleteSingleSuite = 0
	AutoCompleteRangedSuite = 1
	AutoCompletePlaceHolderSuite = 2
	AutoCompleteNoSuite = 3

class ResultCdDescOpt(Enum):
	ResultCodeDescriptionLong = 0
	ResultCodeDescriptionShort = 1

class MailboxLookupMode(Enum):
	MailboxNone = 0
	MailboxExpress = 1
	MailboxPremium = 2

class mdZip(object):
	def __init__(self, encoding, errors):
		self.encoding = encoding
		self.errors = errors
		self.I = lib.mdZipCreate()

	def __del__(self):
		lib.mdZipDestroy(self.I)

	def Initialize(self, p1, p2, p3):
		return ProgramStatus(lib.mdZipInitialize(self.I, p1.encode(self.encoding, errors=self.errors), p2.encode(self.encoding, errors=self.errors), p3.encode(self.encoding, errors=self.errors)))

	def GetInitializeErrorString(self):
		return lib.mdZipGetInitializeErrorString(self.I).decode(self.encoding)

	def GetDatabaseDate(self):
		return lib.mdZipGetDatabaseDate(self.I).decode(self.encoding)

	def GetBuildNumber(self):
		return lib.mdZipGetBuildNumber(self.I).decode(self.encoding)

	def SetLicenseString(self, p1):
		return lib.mdZipSetLicenseString(self.I, p1.encode(self.encoding, errors=self.errors))

	def GetLicenseExpirationDate(self):
		return lib.mdZipGetLicenseExpirationDate(self.I).decode(self.encoding)

	def FindZip(self, p1, p2):
		return lib.mdZipFindZip(self.I, p1.encode(self.encoding, errors=self.errors), p2)

	def FindZipNext(self):
		return lib.mdZipFindZipNext(self.I)

	def FindZipInCity(self, p1, p2):
		return lib.mdZipFindZipInCity(self.I, p1.encode(self.encoding, errors=self.errors), p2.encode(self.encoding, errors=self.errors))

	def FindZipInCityNext(self):
		return lib.mdZipFindZipInCityNext(self.I)

	def FindCityInState(self, p1, p2):
		return lib.mdZipFindCityInState(self.I, p1.encode(self.encoding, errors=self.errors), p2.encode(self.encoding, errors=self.errors))

	def FindCityInStateNext(self):
		return lib.mdZipFindCityInStateNext(self.I)

	def ComputeDistance(self, p1, p2, p3, p4):
		return lib.mdZipComputeDistance(self.I, p1, p2, p3, p4)

	def ComputeBearing(self, p1, p2, p3, p4):
		return lib.mdZipComputeBearing(self.I, p1, p2, p3, p4)

	def GetCountyNameFromFips(self, p1):
		return lib.mdZipGetCountyNameFromFips(self.I, p1.encode(self.encoding, errors=self.errors)).decode(self.encoding)

	def GetSCFArea(self, p1, p2, p3, p4, p5):
		return lib.mdZipGetSCFArea(self.I, p1.encode(self.encoding, errors=self.errors), p2, p3, p4, p5)

	def GetZip(self):
		return lib.mdZipGetZip(self.I).decode(self.encoding)

	def GetCity(self):
		return lib.mdZipGetCity(self.I).decode(self.encoding)

	def GetCityAbbreviation(self):
		return lib.mdZipGetCityAbbreviation(self.I).decode(self.encoding)

	def GetState(self):
		return lib.mdZipGetState(self.I).decode(self.encoding)

	def GetZipType(self):
		return lib.mdZipGetZipType(self.I).decode(self.encoding)

	def GetCountyName(self):
		return lib.mdZipGetCountyName(self.I).decode(self.encoding)

	def GetCountyFips(self):
		return lib.mdZipGetCountyFips(self.I).decode(self.encoding)

	def GetAreaCode(self):
		return lib.mdZipGetAreaCode(self.I).decode(self.encoding)

	def GetLongitude(self):
		return lib.mdZipGetLongitude(self.I).decode(self.encoding)

	def GetLatitude(self):
		return lib.mdZipGetLatitude(self.I).decode(self.encoding)

	def GetTimeZone(self):
		return lib.mdZipGetTimeZone(self.I).decode(self.encoding)

	def GetTimeZoneCode(self):
		return lib.mdZipGetTimeZoneCode(self.I).decode(self.encoding)

	def GetMsa(self):
		return lib.mdZipGetMsa(self.I).decode(self.encoding)

	def GetPmsa(self):
		return lib.mdZipGetPmsa(self.I).decode(self.encoding)

	def GetFacilityCode(self):
		return lib.mdZipGetFacilityCode(self.I).decode(self.encoding)

	def GetLastLineIndicator(self):
		return lib.mdZipGetLastLineIndicator(self.I).decode(self.encoding)

	def GetLastLineNumber(self):
		return lib.mdZipGetLastLineNumber(self.I).decode(self.encoding)

	def GetPreferredLastLineNumber(self):
		return lib.mdZipGetPreferredLastLineNumber(self.I).decode(self.encoding)

	def GetAutomation(self):
		return lib.mdZipGetAutomation(self.I).decode(self.encoding)

	def GetFinanceNumber(self):
		return lib.mdZipGetFinanceNumber(self.I).decode(self.encoding)
