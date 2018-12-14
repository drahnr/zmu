use crate::core::instruction::Imm32Carry;
use crate::core::instruction::Instruction;
use crate::core::operation::thumb_expand_imm_c;
use crate::core::register::Reg;
use bit_field::BitField;
use crate::core::ThumbCode;

#[allow(non_snake_case)]
#[inline]
pub fn decode_BIC_reg_t1(command: u16) -> Instruction {
    Instruction::BIC_reg {
        rd: Reg::from(command.get_bits(0..3)as u8),
        rn: Reg::from(command.get_bits(0..3)as u8),
        rm: Reg::from(command.get_bits(3..6)as u8),
        setflags: true,
    }
}

#[allow(non_snake_case)]
pub fn decode_BIC_reg_t2(opcode: u32) -> Instruction {
    Instruction::UDF {
        imm32: 0,
        opcode: ThumbCode::from(opcode),
    }
}

#[allow(non_snake_case)]
#[inline]
pub fn decode_BIC_imm_t1(opcode: u32) -> Instruction {
    let rd: u8 = opcode.get_bits(8..12) as u8;
    let rn: u8 = opcode.get_bits(16..20) as u8;

    let s: u8 = opcode.get_bit(20) as u8;

    let imm3: u8 = opcode.get_bits(12..15) as u8;
    let imm8: u8 = opcode.get_bits(0..8) as u8;
    let i: u8 = opcode.get_bit(26) as u8;

    let params = [i, imm3, imm8];
    let lengths = [1, 3, 8];

    Instruction::BIC_imm {
        rd: Reg::from(rd),
        rn: Reg::from(rn),
        imm32: Imm32Carry::Carry {
            imm32_c0: thumb_expand_imm_c(&params, &lengths, false),
            imm32_c1: thumb_expand_imm_c(&params, &lengths, true),
        },
        setflags: s == 1,
    }
}
