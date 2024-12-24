import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { extractNumbers } from '../day_13_claw_contraption/solution';

const formatInput = (puzzleInput: string[]) => {
  const A = extractNumbers(puzzleInput[0])[0];
  const program = extractNumbers(puzzleInput[4]);
  return { A, program };
};

const getComboOperand = (operand: number, a: number, b: number, c: number) => {
  switch (operand) {
    case 4:
      return a;
    case 5:
      return b;
    case 6:
      return c;
    default:
      if (operand < 4) return operand;
      throw new Error(`Invalid operand: ${operand}`);
  }
};

const mod = (n: number, m: number) => ((n % m) + m) % m;

const runProgram = (instructions: number[], A: number) => {
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
        registerB = mod(comboOperand, 8);
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
        output.push(mod(comboOperand, 8));
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

  return output;
};

export const partOne = (puzzleInput: string[]) => {
  const { A, program } = formatInput(puzzleInput);
  return runProgram(program, A).join(',');
};

/**
 * Finds the smallest integer `A` such that, when the program is executed with `A`, its output matches the program itself.
 *
 * The function works by iteratively comparing the program's output to its own structure, starting with a single-digit match.
 *
 * - Initially, `A` is set to 0, and the comparison begins from the last digit of the program.
 * - For each test case, `A` is iterated over the range `[startA, startA + 7]`.
 * - If a match is found:
 *   - If the number of matched digits equals the program's length, the correct `A` is returned.
 *   - Otherwise, a new test case is created with:
 *     - An incremented number of digits to compare in the next iteration.
 *     - A new starting value for `A` set to the current `A` multiplied by 8, ensuring proper alignment with program constraints.
 *
 * The function continues until a valid `A` is found or all possibilities are exhausted.
 */
export const partTwo = (puzzleInput: string[]): string => {
  const { program } = formatInput(puzzleInput);
  const queue = [{ digitsToMatch: 1, initialA: 0 }];

  while (queue.length > 0) {
    const { digitsToMatch, initialA } = queue.shift()!;

    for (let A = initialA; A < initialA + 8; A++) {
      const output = runProgram(program, A);
      const targetOutput = program.slice(-digitsToMatch);

      if (output.join() === targetOutput.join()) {
        if (digitsToMatch === program.length) {
          return A.toString();
        }

        queue.push({ digitsToMatch: digitsToMatch + 1, initialA: A * 8 });
      }
    }
  }
  return 'No value for A found to create the input program.';
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('17', 'chronospatial_computer', partOne, partTwo, puzzleInput);
}
