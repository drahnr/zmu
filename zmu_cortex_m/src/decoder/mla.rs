use crate::core::bits::Bits;
use crate::core::instruction::Instruction;
use crate::core::register::Reg;

#[allow(non_snake_case)]
pub fn decode_MLA_t1(opcode: u32) -> Instruction {
    Instruction::MLA {
        rm: Reg::from(opcode.get_bits(0..4) as u8),
        rd: Reg::from(opcode.get_bits(8..12) as u8),
        ra: Reg::from(opcode.get_bits(12..16) as u8),
        rn: Reg::from(opcode.get_bits(16..20) as u8),
    }
}
