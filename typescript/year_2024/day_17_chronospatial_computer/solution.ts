import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { extractNumbers } from '../day_13_claw_contraption/solution';

const formatInput = (puzzleInput: string[]) => {
  const A = extractNumbers(puzzleInput[0])[0];
  const program = extractNumbers(puzzleInput[4]);
  return { A, program };
};

const getComboOperand = (operand: number, A: number, B: number, C: number) => {
  if (operand < 4) return operand;
  if (operand === 4) return A;
  if (operand === 5) return B;
  if (operand === 6) return C;
  return NaN;
};

const runProgram = (instructions: number[], A: number): string => {
  const output = [];
  let registerB = 0;
  let registerC = 0;
  let pointer = 0;

  while (pointer < instructions.length - 1) {
    const opcode = instructions[pointer];
    const operand = instructions[pointer + 1];
    const comboOperand = getComboOperand(operand, A, registerB, registerC);

    switch (opcode) {
      case 0:
        A = Math.floor(A / Math.pow(2, comboOperand));
        pointer += 2;
        break;
      case 1:
        registerB ^= operand;
        pointer += 2;
        break;
      case 2:
        registerB = comboOperand % 8;
        pointer += 2;
        break;
      case 3:
        pointer = A === 0 ? pointer + 2 : operand;
        break;
      case 4:
        registerB ^= registerC;
        pointer += 2;
        break;
      case 5:
        output.push(comboOperand % 8);
        pointer += 2;
        break;
      case 6:
        registerB = Math.floor(A / Math.pow(2, comboOperand));
        pointer += 2;
        break;
      case 7:
        registerC = Math.floor(A / Math.pow(2, comboOperand));
        pointer += 2;
        break;
    }
  }
  return output.join(',');
};

export const partOne = (puzzleInput: string[]) => {
  const { A, program } = formatInput(puzzleInput);
  console.log(program);
  return runProgram(program, A);
};
export const partTwo = (puzzleInput: string[]) => {
  return 'Part 2 Answer';
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('17', 'chronospatial_computer', partOne, partTwo, puzzleInput);
}
