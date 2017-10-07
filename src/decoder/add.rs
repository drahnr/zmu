use bit_field::BitField;

use core::register::Reg;
use core::instruction::Instruction;

#[allow(non_snake_case)]
pub fn decode_ADDS(command: u16) -> Instruction {
    Instruction::ADDS {
        rm: Reg::from_u16(command.get_bits(6..9)).unwrap(),
        rn: Reg::from_u16(command.get_bits(3..6)).unwrap(),
        rd: Reg::from_u16(command.get_bits(0..3)).unwrap(),
    }
}

#[allow(non_snake_case)]
pub fn decode_ADD(command: u16) -> Instruction {
    Instruction::ADD {
        rm: Reg::from_u16(command.get_bits(3..7)).unwrap(),
        rdn: Reg::from_u16(((command.get_bit(7) as u16) << 3) + command.get_bits(0..3)).unwrap(),
    }
}

#[allow(non_snake_case)]
pub fn decode_ADDS_imm_t1(command: u16) -> Instruction {
    Instruction::ADD_imm {
        rd: Reg::from_u16(command.get_bits(0..3)).unwrap(),
        rn: Reg::from_u16(command.get_bits(3..6)).unwrap(),
        imm32: command.get_bits(6..9) as u32,
        setflags : true
    }
}

#[allow(non_snake_case)]
pub fn decode_ADDS_imm_t2(command: u16) -> Instruction {
    Instruction::ADD_imm {
        rn: Reg::from_u16(command.get_bits(8..11)).unwrap(),
        rd: Reg::from_u16(command.get_bits(8..11)).unwrap(),
        imm32: command.get_bits(0..8) as u32,
        setflags : true
    }
}

#[allow(non_snake_case)]
pub fn decode_ADD_SP_imm_t1(command: u16) -> Instruction {
    Instruction::ADD_imm {
        rd: Reg::from_u16(command.get_bits(8..11)).unwrap(),
        rn: Reg::SP,
        imm32: (command.get_bits(0..8) as u32) << 2,
        setflags : false
    }
}

#[allow(non_snake_case)]
pub fn decode_ADD_SP_imm_t2(command: u16) -> Instruction {
    Instruction::ADD_imm {
        rd: Reg::SP,
        rn: Reg::SP,
        imm32: (command.get_bits(0..7) as u32) << 2,
        setflags : false
    }
}
