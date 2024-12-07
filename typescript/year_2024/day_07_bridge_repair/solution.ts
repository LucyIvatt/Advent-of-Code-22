import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { generateCombinations } from '../../utils/misc';

export const partOne = (puzzle_input: string[]) => {
  const formatted_input = puzzle_input.map((a) => {
    const s = a.split(':');
    return { output: Number(s[0]), equation: s[1].split(' ').splice(1) };
  });
  let validEquations = 0;

  for (const { output, equation } of formatted_input) {
    for (const combination of generateCombinations(['*', '+'], equation.length - 1)) {
      let total = Number(equation[0]);
      for (let i = 0; i < combination.length; i++) {
        total = eval(total.toString() + combination[i] + equation[i + 1]);
        if (total > output) break;
      }
      if (total === output) {
        validEquations += output;
        break;
      }
    }
  }

  return validEquations.toString();
};

export const partTwo = (puzzle_input: string[]) => {
  const formatted_input = puzzle_input.map((a) => {
    const s = a.split(':');
    return { output: Number(s[0]), equation: s[1].split(' ').splice(1) };
  });
  let validEquations = 0;

  for (const { output, equation } of formatted_input) {
    for (const combination of generateCombinations(['*', '+', '|'], equation.length - 1)) {
      let total = Number(equation[0]);
      for (let i = 0; i < combination.length; i++) {
        if (combination[i] === '|') total = Number(total.toString() + equation[i + 1]);
        else total = eval(total.toString() + combination[i] + equation[i + 1]);
        if (total > output) break;
      }
      if (total === output) {
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
