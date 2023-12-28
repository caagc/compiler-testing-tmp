#include <iostream>
#include <cstring>
#include <map>
#include <cstring>
#include <vector>
using namespace std;

enum CntName {
	pMoreStructUnionCnt,
	pBitFieldsCreationCnt,
	pBitFieldsSignedCnt,
	pBitFieldInNormalStructCnt,
	pScalarFieldInFullBitFieldsCnt,
	pExhaustiveBitFieldsCnt,
	pSafeOpsSignedCnt,
	pSelectDerefPointerCnt,
	pRegularVolatileCnt,
	pRegularConstCnt,
	pStricterConstCnt,
	pLooserConstCnt,
	pFieldVolatileCnt,
	pFieldConstCnt,
	pStdUnaryFuncCnt,
	pShiftByNonConstantCnt,
	pPointerAsLTypeCnt,
	pStructAsLTypeCnt,
	pUnionAsLTypeCnt,
	pFloatAsLTypeCnt,
	pNewArrayVariableCnt,
	pAccessOnceVariableCnt,
	pInlineFunctionCnt,
	pBuiltinFunctionCnt,

	// group for statement
	// pStatementCnt,
	pAssignCnt,
	pBlockCnt,
	pForCnt,
	pIfElseCnt,
	pInvokeCnt,
	pReturnCnt,
	pContinueCnt,
	pBreakCnt,
	pGotoCnt,
	pArrayOpCnt,

	// group for assignment ops
	// pAssignOpsCnt,
	pSimpleAssignCnt,
	pMulAssignCnt,
	pDivAssignCnt,
	pRemAssignCnt,
	pAddAssignCnt,
	pSubAssignCnt,
	pLShiftAssignCnt,
	pRShiftAssignCnt,
	pBitAndAssignCnt,
	pBitXorAssignCnt,
	pBitOrAssignCnt,
	pPreIncrCnt,
	pPreDecrCnt,
	pPostIncrCnt,
	pPostDecrCnt,

	// for unary ops
	// pUnaryOpsCnt,
	pPlusCnt,
	pMinusCnt,
	pNotCnt,
	pBitNotCnt,

	// for binary ops
	// pBinaryOpsCnt,
	pAddCnt,
	pSubCnt,
	pMulCnt,
	pDivCnt,
	pModCnt,
	pCmpGtCnt,
	pCmpLtCnt,
	pCmpGeCnt,
	pCmpLeCnt,
	pCmpEqCnt,
	pCmpNeCnt,
	pAndCnt,
	pOrCnt,
	pBitXorCnt,
	pBitAndCnt,
	pBitOrCnt,
	pRShiftCnt,
	pLShiftCnt,

	// group for simple types
	// pSimpleTypesCnt,
	pVoidCnt,
	pCharCnt,
	pIntCnt,
	pShortCnt,
	pLongCnt,
	pLongLongCnt,
	pUCharCnt,
	pUIntCnt,
	pUShortCnt,
	pULongCnt,
	pULongLongCnt,
	pFloatCnt,

	// for safe math ops
	// pSafeOpsSizeCnt,
	pInt8Cnt,
	pInt16Cnt,
	pInt32Cnt,
	pInt64Cnt,

	pMoreStructUnionTotalCnt,
	pBitFieldsCreationTotalCnt,
	pBitFieldsSignedTotalCnt,
	pBitFieldInNormalStructTotalCnt,
	pScalarFieldInFullBitFieldsTotalCnt,
	pExhaustiveBitFieldsTotalCnt,
	pSafeOpsSignedTotalCnt,
	pSelectDerefPointerTotalCnt,
	pRegularVolatileTotalCnt,
	pRegularConstTotalCnt,
	pStricterConstTotalCnt,
	pLooserConstTotalCnt,
	pFieldVolatileTotalCnt,
	pFieldConstTotalCnt,
	pStdUnaryFuncTotalCnt,
	pShiftByNonConstantTotalCnt,
	pPointerAsLTypeTotalCnt,
	pStructAsLTypeTotalCnt,
	pUnionAsLTypeTotalCnt,
	pFloatAsLTypeTotalCnt,
	pNewArrayVariableTotalCnt,
	pAccessOnceVariableTotalCnt,
	pInlineFunctionTotalCnt,
	pBuiltinFunctionTotalCnt,

};


class Record {
public:

	static void initialize();

	static void initialize_tmp();

	static void set_name_cnt(string pname, int cnt);

	static void set_name_cnt_tmp(string pname, int cnt);

	static void print_name_cnt();

	static void print_name_cnt_tmp();

	static void group_feature_append(CntName start, CntName end, vector<float>& target);

	static void print_feature();

	static void print();

	static void set_csmith_cnt_file(string file);

	static string cntName[111];

	static string csmith_cnt_file;

	static std::map<string, int> pname_to_cnt;

	static std::map<string, int> tmp_pname_to_cnt;

	Record();

	~Record();
};

