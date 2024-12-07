import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { generateCombinations } from '../../utils/misc';

const parseInput = (puzzle_input: string[]) =>
  puzzle_input.map((line) => {
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

const findCalibrationResult = (puzzle_input: string[], operators: string[]) => {
  return parseInput(puzzle_input).reduce((sum, { output, equation }) => {
    for (const combination of generateCombinations(operators, equation.length - 1)) {
      if (evaluateEquation(equation, Array.from(combination), output)) {
        return sum + output;
      }
    }
    return sum;
  }, 0);
};

export const partOne = (puzzle_input: string[]) => {
  return findCalibrationResult(puzzle_input, ['*', '+']).toString();
};

export const partTwo = (puzzle_input: string[]) => {
  return findCalibrationResult(puzzle_input, ['*', '+', '|']).toString();
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('07', 'bridge_repair', partOne, partTwo, puzzle_input);
}
