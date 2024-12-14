import path from 'path';
import { InputFile, readPuzzleInput, split2DArray } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

const cramersRule = (buttonA: number[], buttonB: number[], prize: number[]) => {
  const a = (prize[0] * buttonB[1] - prize[1] * buttonB[0]) / (buttonA[0] * buttonB[1] - buttonA[1] * buttonB[0]);
  const b = (buttonA[0] * prize[1] - buttonA[1] * prize[0]) / (buttonA[0] * buttonB[1] - buttonA[1] * buttonB[0]);
  return { a, b };
};

const calculateTokens = (machines: string[][], updatedPositons = false) => {
  let tokensSpent = 0;

  for (const machine of machines) {
    const buttonA = machine[0].match(/\d+/g)!.map(Number);
    const buttonB = machine[1].match(/\d+/g)!.map(Number);
    const prize = machine[2].match(/\d+/g)!.map(Number);

    if (updatedPositons) {
      prize[0] += 10_000_000_000_000;
      prize[1] += 10_000_000_000_000;
    }

    const { a, b } = cramersRule(buttonA, buttonB, prize);

    if (a % 1 == 0 && b % 1 == 0) {
      tokensSpent += 3 * a + b;
    }
  }
  return tokensSpent;
};

export const partOne = (puzzleInput: string[]) => {
  const machines = split2DArray(puzzleInput, '');
  return calculateTokens(machines).toString();
};

export const partTwo = (puzzleInput: string[]) => {
  const machines = split2DArray(puzzleInput, '');
  return calculateTokens(machines, true).toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('13', 'claw_contraption', partOne, partTwo, puzzleInput);
}
