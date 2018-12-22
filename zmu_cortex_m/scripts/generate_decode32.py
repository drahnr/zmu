""" Module for autogenerating ARMv6-m decoder trees"""


INSTRUCTIONS = {

    '11111110...1...............1....': 'MRC2_t2',
    '11111110...0...............0....': 'MCR2_t2',
    '11111110...................0....': 'CDP2_t2',
    '111111000100....................': 'MCRR2_t2',
    '1111110....11111................': 'LDC2_lit_t2',
    '1111110....1....................': 'LDC2_imm_t2',
    '1111110....0....................': 'STC2_t2',
    '111110111110............0000....': 'UMLAL_t1',
    '111110111100............0000....': 'SMLAL_t1',
    '111110111011....1111....1111....': 'UDIV_t1',
    '111110111010............0000....': 'UMULL_t1',
    '111110111001....1111....1111....': 'SDIV_t1',
    '111110111000............0000....': 'SMULL_t1',
    '111110110000....1111....0000....': 'MUL_t2',
    '111110110000............0001....': 'MLS_t1',
    '111110110000............0000....': 'MLA_t1',
    '111110101011....1111....1000....': 'CLZ_t1',
    '111110101001....1111....1011....': 'REVSH_t2',
    '111110101001....1111....1010....': 'RBIT_t1',
    '111110101001....1111....1001....': 'REV16_t2',
    '111110101001....1111....1000....': 'REV_t2',
    '11111010011.....1111....0000....': 'ROR_reg_t2',
    '11111010010111111111....10......': 'UXTB_t2',
    '11111010010011111111....10......': 'SXTB_t2',
    '11111010010.....1111....0000....': 'ASR_reg_t2',
    '11111010001.....1111....0000....': 'LSR_reg_t2',
    '11111010000111111111....10......': 'UXTH_t2',
    '11111010000011111111....10......': 'SXTH_t2',
    '11111010000.....1111....0000....': 'LSL_reg_t2',
    '111110011011....................': 'LDRSH_imm_t1',
    '111110011001....1111............': 'PLI_lit_imm_t1',
    '111110011001....................': 'LDRSB_imm_t1',
    '111110010011........1110........': 'LDRSHT',
    '111110010011........1...........': 'LDRSH_imm_t2',
    '111110010011........000000......': 'LDRSH_reg_t2',
    '111110010001....11111100........': 'PLI_lit_imm_t2',
    '111110010001....1111000000......': 'PLI_reg_t1',
    '111110010001........1110........': 'LDRSBT_t1',
    '111110010001........1...........': 'LDRSB_imm_t2',
    '111110010000........000000......': 'LDRSB_reg_t2',
    '11111001.0111111................': 'LDRSH_lit_t1',
    '11111001.00111111111............': 'PLI_lit_imm_t3',
    '11111001.0011111................': 'LDRSB_lit_t1',
    '111110001101....................': 'LDR_imm_t3',
    '111110001100....................': 'STR_imm_t3',
    '111110001011....................': 'LDRH_imm_t2',
    '111110001010....................': 'STRH_imm_t2',
    '111110001001....1111............': 'PLD_imm_t1',
    '111110001001....................': 'LDRB_imm_t2',
    '111110001000....................': 'STRB_imm_t2',
    '1111100001011101....101100000100': 'POP_t3',
    '111110000101........1110........': 'LDRT_t1',
    '111110000101........1...........': 'LDR_imm_t4',
    '111110000101........000000......': 'LDR_reg_t2',
    '1111100001001101....110100000100': 'PUSH_t3',
    '111110000100........1...........': 'STR_imm_t4',
    '111110000100........000000......': 'STR_reg_t2',
    '111110000011........1110........': 'LDRHT_t1',
    '111110000011........1...........': 'LDRH_imm_t3',
    '111110000011........000000......': 'LDRH_reg_t2',
    '111110000010........1...........': 'STRH_imm_t3',
    '111110000001....11111100........': 'PLD_imm_t2',
    '111110000001........1110........': 'LDRBT_t1',
    '111110000001........1...........': 'LDRB_imm_t3',
    '111110000001........00000.......': 'LDRB_reg_t2',
    '111110000010........000000......': 'STRH_reg_t2',
    '111110000000........1...........': 'STRB_imm_t3',
    '111110000000........000000......': 'STRB_reg_t2',
    '11111000.1011111................': 'LDR_lit_t2',
    '11111000.0111111................': 'LDRH_lit_t1',
    '11111000.0011111................': 'LDRB_lit_t1',
    '111101111111....1010............': 'UDF_t2',
    '11110011111011111000............': 'MRS_t1',
    '111100111100....0.........0.....': 'UBFX_t1',
    '1111001110111111100011110110....': 'ISB_t1',
    '1111001110111111100011110101....': 'DMB_t1',
    '1111001110111111100011110100....': 'DSB_t1',
    '1111001110111111100011110010....': 'CLREX_t1',
    '11110011101011111000000011110000': 'DBG_t1',
    '11110011101011111000000000000100': 'SEV_t2',
    '11110011101011111000000000000011': 'WFI_t2',
    '11110011101011111000000000000010': 'WFE_t2',
    '11110011101011111000000000000001': 'YIELD_t2',
    '11110011101011111000000000000000': 'NOP_t2',
    '111100111000....10001000........': 'MSR_reg_t1',
    '1111001110.0....0.........0.....': 'USAT_t1',
    '11110011011011110.........0.....': 'BFC_t1',
    '111100110110....0.........0.....': 'BFI_t1',
    '111100110100....0.........0.....': 'SBFX_t1',
    '1111001100.0....0.........0.....': 'SSAT_t1',
    '11110.101100....0...............': 'MOVT_t1',
    '11110.10101011110...............': 'ADR_t2',
    '11110.101010....0...............': 'SUB_imm_t4',
    '11110.100100....0...............': 'MOV_imm_t3',
    '11110.10000011110...............': 'ADR_t3',
    '11110.100000....0...............': 'ADD_imm_t4',
    '11110.01110.....0...............': 'RSB_imm_t2',
    '11110.011011....0...1111........': 'CMP_imm_t2',
    '11110.01101.....0...............': 'SUB_imm_t3',
    '11110.01011.....0...............': 'SBC_imm_t1',
    '11110.01101.11010...............': 'SUB_SP_imm_t2',
    '11110.10101011010...............': 'SUB_SP_imm_t3',
    '11110.01010.....0...............': 'ADC_imm_t1',
    '11110.010001....0...1111........': 'CMN_imm_t1',
    '11110.01000.....0...............': 'ADD_imm_t3',
    '11110.001001....0...1111........': 'TEQ_imm_t1',
    '11110.00100.....0...............': 'EOR_imm_t1',
    '11110.00011.11110...............': 'MVN_imm_t1',
    '11110.00011.....0...............': 'ORN_imm_t1',
    '11110.00010.....0...............': 'ORR_imm_t1',
    '11110.00010.11110...............': 'MOV_imm_t2',
    '11110.000001....0...1111........': 'TST_imm_t1',
    '11110.00001.....0...............': 'BIC_imm_t1',
    '11110.00000.....0...............': 'AND_imm_t1',
    '11110...........11.1............': 'BL_t1',
    '11110...........10.1............': 'B_t4',
    '11110...........10.0............': 'B_t3',
    '11101110...1...............1....': 'MRC_t1',
    '11101110...0...............0....': 'MCR_t1',
    '11101110...................0....': 'CDP_t1',
    '111011000100....................': 'MCRR_t1',
    '1110110....11111................': 'LDC_lit_t1',
    '1110110....1....................': 'LDC_imm_t1',
    '1110110....0....................': 'STC_t1',
    '11101011110.....0...............': 'RSB_reg_t1',
    '111010111011....0...1111........': 'CMP_reg_t3',
    '11101011101.....0...............': 'SUB_reg_t2',
    '11101011011.....0...............': 'SBC_reg_t2',
    '11101011010.....0...............': 'ADC_reg_t2',
    '111010110001....0...1111........': 'CMN_reg_t2',
    '11101011000.....0...............': 'ADD_reg_t3',
    '111010101001....0...1111........': 'TEQ_reg_t1',
    '11101010100.....0...............': 'EOR_reg_t2',
    '11101010011.11110...............': 'MVN_reg_t2',
    '11101010011.....0...............': 'ORN_reg_t2',
    '11101010010.11110000....0011....': 'RRX_t1',
    '11101010010.11110000....0000....': 'MOV_reg_t3',
    '11101010010.11110.........11....': 'ROR_imm_t1',
    '11101010010.11110.........10....': 'ASR_imm_t2',
    '11101010010.11110.........01....': 'LSR_imm_t2',
    '11101010010.11110.........00....': 'LSL_imm_t2',
    '11101010010.....0...............': 'ORR_reg_t2',
    '11101010001.....0...............': 'BIC_reg_t2',
    '111010100001....0...1111........': 'TST_reg_t2',
    '11101010000.....0...............': 'AND_reg_t2',
    '11101001001011010.0.............': 'PUSH_t2',
    '1110100100.1......0.............': 'LDMDB_t1',
    '1110100100.0....0.0.............': 'STMDB_t1',
    '111010001101....111100000001....': 'TBH_t1',
    '111010001101....111100000000....': 'TBB_t1',
    '111010001101........111101011111': 'LDREXH_t1',
    '111010001101........111101001111': 'LDREXB_t1',
    '111010001100........11110101....': 'STREXH_t1',
    '111010001100........11110100....': 'STREXB_t1',
    '1110100010111101..0.............': 'POP_t2',
    '1110100010.1......0.............': 'LDM_t2',
    '1110100010.0....0.0.............': 'STM_t2',
    '111010000101........1111........': 'LDREX_t1',
    '111010000100....................': 'STREX_t1',
    '1110100..1.11111................': 'LDRD_lit_t1',
    '1110100..1.1....................': 'LDRD_imm_t1',
    '1110100..1.0....................': 'STRD_imm_t1',

}


def main():
    """ My main function"""

    #
    # finding a decoder match:
    # - go through the list of bitmasks in the order of specificity
    #   - test first the ones that have most bits set
    #   - first one to match is the one
    #
    maskstrings = sorted(INSTRUCTIONS.iterkeys(),
                         key=lambda string: string.count('.'))
    onemasks = [key.replace('0', '1')
                for key in maskstrings]
    onemasks = [int(key.replace('.', '0'), 2)
                for key in onemasks]
    resultmasks = [int(key.replace('.', '0'), 2)
                   for key in maskstrings]

    for i in range(len(onemasks)):
        onemask = onemasks[i]
        result = resultmasks[i]
        instr = INSTRUCTIONS[maskstrings[i]]
        if onemask == 0xffffffff:
            print '{} if opcode == 0x{:x} {{ decode_{}(opcode)}}'.format('' if i == 0 else 'else', result, instr)
        else:
            print '{} if (opcode & 0x{:x}) == 0x{:x} {{ decode_{}(opcode)}}'.format('' if i == 0 else 'else', onemask, result, instr)


main()
