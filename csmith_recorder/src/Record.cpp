#include <iostream>
#include "Record.h"
#include <map>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <cassert>

using namespace std;

std::map<string, int> Record::pname_to_cnt = std::map<string, int>();
std::map<string, int> Record::tmp_pname_to_cnt = std::map<string, int>();

string Record::cntName[111] = {"pMoreStructUnionCnt","pBitFieldsCreationCnt","pBitFieldsSignedCnt","pBitFieldInNormalStructCnt","pScalarFieldInFullBitFieldsCnt","pExhaustiveBitFieldsCnt","pSafeOpsSignedCnt","pSelectDerefPointerCnt","pRegularVolatileCnt","pRegularConstCnt","pStricterConstCnt","pLooserConstCnt","pFieldVolatileCnt","pFieldConstCnt","pStdUnaryFuncCnt","pShiftByNonConstantCnt","pPointerAsLTypeCnt","pStructAsLTypeCnt","pUnionAsLTypeCnt","pFloatAsLTypeCnt","pNewArrayVariableCnt","pAccessOnceVariableCnt","pInlineFunctionCnt","pBuiltinFunctionCnt","pAssignCnt","pBlockCnt","pForCnt","pIfElseCnt","pInvokeCnt","pReturnCnt","pContinueCnt","pBreakCnt","pGotoCnt","pArrayOpCnt","pSimpleAssignCnt","pMulAssignCnt","pDivAssignCnt","pRemAssignCnt","pAddAssignCnt","pSubAssignCnt","pLShiftAssignCnt","pRShiftAssignCnt","pBitAndAssignCnt","pBitXorAssignCnt","pBitOrAssignCnt","pPreIncrCnt","pPreDecrCnt","pPostIncrCnt","pPostDecrCnt","pPlusCnt","pMinusCnt","pNotCnt","pBitNotCnt","pAddCnt","pSubCnt","pMulCnt","pDivCnt","pModCnt","pCmpGtCnt","pCmpLtCnt","pCmpGeCnt","pCmpLeCnt","pCmpEqCnt","pCmpNeCnt","pAndCnt","pOrCnt","pBitXorCnt","pBitAndCnt","pBitOrCnt","pRShiftCnt","pLShiftCnt","pVoidCnt","pCharCnt","pIntCnt","pShortCnt","pLongCnt","pLongLongCnt","pUCharCnt","pUIntCnt","pUShortCnt","pULongCnt","pULongLongCnt","pFloatCnt","pInt8Cnt","pInt16Cnt","pInt32Cnt","pInt64Cnt","pMoreStructUnionTotalCnt","pBitFieldsCreationTotalCnt","pBitFieldsSignedTotalCnt","pBitFieldInNormalStructTotalCnt","pScalarFieldInFullBitFieldsTotalCnt","pExhaustiveBitFieldsTotalCnt","pSafeOpsSignedTotalCnt","pSelectDerefPointerTotalCnt","pRegularVolatileTotalCnt","pRegularConstTotalCnt","pStricterConstTotalCnt","pLooserConstTotalCnt","pFieldVolatileTotalCnt","pFieldConstTotalCnt","pStdUnaryFuncTotalCnt","pShiftByNonConstantTotalCnt","pPointerAsLTypeTotalCnt","pStructAsLTypeTotalCnt","pUnionAsLTypeTotalCnt","pFloatAsLTypeTotalCnt","pNewArrayVariableTotalCnt","pAccessOnceVariableTotalCnt","pInlineFunctionTotalCnt","pBuiltinFunctionTotalCnt"};

string Record::csmith_cnt_file = "./csmith_cnt.csv";
//87 111
Record::Record()
{

}

Record::~Record()
{

}

void
Record::initialize()
{
	for(int i = 0; i < 111; i++)
	{
		pname_to_cnt[cntName[i]] = 0;
	}
}

void
Record::initialize_tmp()
{
	for(int i = 0; i < 111; i++)
	{
		tmp_pname_to_cnt[cntName[i]] = 0;
	}
}

void
Record::set_name_cnt(string pname, int cnt)
{
	pname_to_cnt[pname] += cnt;
}

void
Record::set_name_cnt_tmp(string pname, int cnt)
{
	tmp_pname_to_cnt[pname] += cnt;
}

void Record::group_feature_append(CntName start, CntName end, vector<float>& target) {
	int total = 0;
	for(int i = start; i <= end; i++) {
		if (i == pInvokeCnt) continue;
		total += pname_to_cnt[cntName[i]];
	}
	if(total == 0) {
		for(int i = start; i <= end; i++) {
			if (i == pInvokeCnt) continue;
			target.push_back(-1);
		}
	} else {
		for(int i = start; i <= end; i++) {
			if (i == pInvokeCnt) continue;
			target.push_back((float)pname_to_cnt[cntName[i]] * 100.0 / (float)total);
		}
	}
}

void Record::print_feature() {
	vector<float> name_cnt;
	int diff = pMoreStructUnionTotalCnt - pMoreStructUnionCnt;
	for(int i = pMoreStructUnionCnt; i <= pBuiltinFunctionCnt; i++)
	{
		int j = i + diff;
		int cnt = pname_to_cnt[cntName[i]], base = pname_to_cnt[cntName[j]];
		assert(cnt <= base);
		if(base == 0) {
			name_cnt.push_back(-1);
		} else {
			name_cnt.push_back((float)cnt * 100.0 / (float)base);
		}
	}
	group_feature_append(pAssignCnt, pArrayOpCnt, name_cnt);
	group_feature_append(pPlusCnt, pBitNotCnt, name_cnt);
	group_feature_append(pAddCnt, pLShiftCnt, name_cnt);
	group_feature_append(pVoidCnt, pFloatCnt, name_cnt);
	group_feature_append(pInt8Cnt, pInt64Cnt, name_cnt);

	
	assert(name_cnt.size() == 71);
	ofstream ofile;
	// ofile.open(csmith_cnt_file.c_str(),ios::app);
	ofile.open(csmith_cnt_file.c_str());
	for(int i = 0; i < name_cnt.size() - 1; i++)
	{
		ofile<<name_cnt[i]<<",";
	}
	ofile<<name_cnt[name_cnt.size() - 1]<<endl;
	ofile.close();
}


void Record::print() {
	print_feature();
}

void
Record::print_name_cnt()
{
	
	ofstream ofile;
	ofile.open(csmith_cnt_file.c_str(),ios::app);

	// for(int i = 0; i < 110; i++)
	// {
	// 	ofile<<cntName[i]<<",";
	// }
	// ofile<<cntName[110]<<endl;

	for(int i = 0; i < 110; i++)
	{
		ofile<<pname_to_cnt[cntName[i]]<<",";
	}
	ofile<<pname_to_cnt[cntName[110]]<<endl;
	
	ofile.close();
}

void
Record::print_name_cnt_tmp()
{
	for(int i = 0; i < 111; i++)
	{
		cout<<cntName[i]<<" ===== "<<tmp_pname_to_cnt[cntName[i]]<<endl;
	}
}


void
Record::set_csmith_cnt_file(string file)
{
	csmith_cnt_file = file;
}