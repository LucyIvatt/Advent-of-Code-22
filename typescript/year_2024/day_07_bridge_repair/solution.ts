import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { generateCombinations } from '../../utils/misc';

const formatInput = (puzzle_input: string[]) => {
  return puzzle_input.map((a) => {
    const s = a.split(':');
    return { output: Number(s[0]), equation: s[1].split(' ').splice(1).map(Number) };
  });
};

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

export const partOne = (puzzle_input: string[]) => {
  let validEquations = 0;
  for (const { output, equation } of formatInput(puzzle_input)) {
    for (const combination of generateCombinations(['*', '+'], equation.length - 1)) {
      if (evaluateEquation(equation, Array.from(combination), output)) {
        validEquations += output;
        break;
      }
    }
  }
  return validEquations.toString();
};

export const partTwo = (puzzle_input: string[]) => {
  let validEquations = 0;
  for (const { output, equation } of formatInput(puzzle_input)) {
    for (const combination of generateCombinations(['*', '+', '|'], equation.length - 1)) {
      if (evaluateEquation(equation, Array.from(combination), output)) {
        validEquations += output;
        break;
      }
    }
  }

  return validEquations.toString();
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('07', 'bridge_repair', partOne, partTwo, puzzle_input);
}
