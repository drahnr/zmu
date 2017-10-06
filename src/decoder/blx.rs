use bit_field::BitField;
use core::register::Reg;
use core::instruction::Op;

#[allow(non_snake_case)]
pub fn decode_BLX(command: u16) -> Op {
    Op::BLX { rm: Reg::from_u16(command.get_bits(3..7) as u16).unwrap() }
}
