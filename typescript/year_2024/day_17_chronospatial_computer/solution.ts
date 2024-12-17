import path, { join } from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { extractNumbers } from '../day_13_claw_contraption/solution';
import { SQRT1_2 } from 'mathjs';

const formatInput = (puzzleInput: string[]) => {
  const [A, B, C] = puzzleInput.filter((line, i) => i < 3).map((line) => extractNumbers(line)[0]);
  const program = extractNumbers(puzzleInput[4]);
  return { A, B, C, program };
};

const getComboOperand = (operand: number, A: number, B: number, C: number) => {
  if (operand < 4) return operand;
  if (operand === 4) return A;
  if (operand === 5) return B;
  if (operand === 6) return C;
  return NaN;
};

export const partOne = (puzzleInput: string[]) => {
  const program = [2, 4, 1, 3, 7, 5, 1, 5, 0, 3, 4, 3, 5, 5, 3, 0];
  const output = [];

  let A = 47006051;
  let B = 0;
  let C = 0;
  let pointer = 0;

  while (pointer < program.length - 1) {
    const opcode = program[pointer];
    const operand = program[pointer + 1];

    switch (opcode) {
      case 0: {
        // adv instruction
        A = Math.floor(A / Math.pow(2, getComboOperand(operand, A, B, C)));
        pointer += 2;
        break;
      }
      case 1: {
        // bxl instruction
        B = B ^ operand;
        pointer += 2;
        break;
      }
      case 2: {
        // bst instruction
        const combo = getComboOperand(operand, A, B, C);
        B = combo % 8;
        pointer += 2;
        break;
      }
      case 3: {
        // jnz instruction
        if (A === 0) pointer += 2;
        else pointer = operand;
        break;
      }
      case 4: {
        // bxc instruction
        B = B ^ C;
        pointer += 2;
        break;
      }
      case 5: {
        // out instruction
        const combo = getComboOperand(operand, A, B, C);
        output.push(combo % 8);
        pointer += 2;
        break;
      }
      case 6: {
        // bdv instruction
        B = Math.floor(A / Math.pow(2, getComboOperand(operand, A, B, C)));
        pointer += 2;
        break;
      }
      case 7: {
        // cdv instruction
        C = Math.floor(A / Math.pow(2, getComboOperand(operand, A, B, C)));
        pointer += 2;
        break;
      }
    }
  }

  console.log('A', A);
  console.log('B', B);
  console.log('C', C);
  console.log(output.join(','));

  return 'Part 1 Answer';
};

export const partTwo = (puzzleInput: string[]) => {
  return 'Part 2 Answer';
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('17', 'chronospatial_computer', partOne, partTwo, puzzleInput);
}
