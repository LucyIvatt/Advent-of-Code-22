import path from 'path';
import { InputFile, readPuzzleInput, split2DArray } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

export const extractNumbers = (input: string): number[] => {
  return (input.match(/\d+/g) || []).map(Number);
};

// An explicit formula for the solution of a system of linear equations
const cramersRule = (buttonA: number[], buttonB: number[], prize: number[]) => {
  const a = (prize[0] * buttonB[1] - prize[1] * buttonB[0]) / (buttonA[0] * buttonB[1] - buttonA[1] * buttonB[0]);
  const b = (buttonA[0] * prize[1] - buttonA[1] * prize[0]) / (buttonA[0] * buttonB[1] - buttonA[1] * buttonB[0]);
  return { a, b };
};

const calculateTokens = (machines: string[][], updatedPositons = false) => {
  let tokensSpent = 0;

  for (const machine of machines) {
    const [buttonA, buttonB, prize] = machine.map(extractNumbers);

    if (updatedPositons) {
      prize[0] += 10_000_000_000_000;
      prize[1] += 10_000_000_000_000;
    }

    const { a, b } = cramersRule(buttonA, buttonB, prize);

    if (Number.isInteger(a) && Number.isInteger(b)) {
      tokensSpent += 3 * a + b;
    }
  }
  return tokensSpent;
};

export const partOne = (puzzleInput: string[]) => {
  return calculateTokens(split2DArray(puzzleInput, '')).toString();
};

export const partTwo = (puzzleInput: string[]) => {
  return calculateTokens(split2DArray(puzzleInput, ''), true).toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('13', 'claw_contraption', partOne, partTwo, puzzleInput);
}
