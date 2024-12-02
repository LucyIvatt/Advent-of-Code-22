import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { functionTimer } from '../../utils/time';

const formatArrays = (puzzle_input: string[]): number[][] => {
  return puzzle_input.map((report) => report.split(' ').map(Number));
};

const isSafeReport = (report: number[]) => {
  const differences = report.slice(0, -1).map((level, index) => {
    return level - report[index + 1];
  });

  return (
    (differences.every((level) => level > 0) || differences.every((level) => level < 0)) && // all increasing or all decreasing
    differences.every((diff) => 0 < Math.abs(diff) && Math.abs(diff) < 4)
  );
};

export const partOne = (puzzle_input: string[]) => {
  return formatArrays(puzzle_input)
    .filter((report) => isSafeReport(report))
    .length.toString();
};

export const partTwo = (puzzle_input: string[]) => {
  const formatted_puzzle = formatArrays(puzzle_input);
  let numSafe = 0;

  for (const report of formatted_puzzle) {
    if (isSafeReport(report)) {
      numSafe += 1;
      continue;
    }

    for (let i = 0; i < report.length; i++) {
      const modifiedReport = [...report.slice(0, i), ...report.slice(i + 1)];
      console.log(modifiedReport);
      if (isSafeReport(modifiedReport)) {
        numSafe += 1;
        break;
      }
    }
  }
  return numSafe.toString();
};

const run = () => {
  const mode = InputFile.INPUT;
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, mode));

  const { output: p1_output, time: p1_time } = functionTimer(partOne, puzzle_input);
  const { output: p2_output, time: p2_time } = functionTimer(partTwo, puzzle_input);

  console.log('--------------------------------------');
  console.log('Day 02: red_nosed_reports');
  console.log('--------------------------------------');
  console.log(`Part One Answer: ${p1_output} - [${p1_time} seconds]`);
  console.log(`Part Two Answer: ${p2_output} - [${p2_time} seconds]`);
  console.log('--------------------------------------');
};

if (require.main === module) {
  run();
}
