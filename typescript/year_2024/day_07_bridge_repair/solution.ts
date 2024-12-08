import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { generateCombinations } from '../../utils/misc';

const parseInput = (puzzleInput: string[]) =>
  puzzleInput.map((line) => {
    const [output, equation] = line.split(':');
    return {
      output: Number(output),
      equation: equation.trim().split(' ').map(Number)
    };
  });

const evaluateEquation = (numbers: number[], operators: string[], target: number) => {
  let total = numbers[0];
  for (let i = 0; i < operators.length; i++) {
    const nextNum = numbers[i + 1];
    switch (operators[i]) {
      case '+':
        total += nextNum;
        break;
      case '*':
        total *= nextNum;
        break;
      case '|':
        total = Number(`${total}${nextNum}`);
        break;
    }
    if (total > target) return false;
  }
  return total === target;
};

const findCalibrationResult = (puzzleInput: string[], operators: string[]) => {
  return parseInput(puzzleInput).reduce((sum, { output, equation }) => {
    for (const combination of generateCombinations(operators, equation.length - 1)) {
      if (evaluateEquation(equation, Array.from(combination), output)) {
        return sum + output;
      }
    }
    return sum;
  }, 0);
};

export const partOne = (puzzleInput: string[]) => {
  return findCalibrationResult(puzzleInput, ['*', '+']).toString();
};

export const partTwo = (puzzleInput: string[]) => {
  return findCalibrationResult(puzzleInput, ['*', '+', '|']).toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('07', 'bridge_repair', partOne, partTwo, puzzleInput);
}
