import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

const parseReports = (puzzleInput: string[]): number[][] => {
  return puzzleInput.map((report) => report.split(' ').map(Number));
};

const isMonotonic = (diffs: number[]) => diffs.every((level) => level > 0) || diffs.every((level) => level < 0);
const isWithinRange = (diffs: number[], lb: number, ub: number) =>
  diffs.every((diff) => Math.abs(diff) >= lb && Math.abs(diff) <= ub);

const isSafeReport = (report: number[]): boolean => {
  const diffs = report.slice(0, -1).map((level, index) => level - report[index + 1]);
  return isMonotonic(diffs) && isWithinRange(diffs, 1, 3);
};

export const partOne = (puzzleInput: string[]): string => {
  return parseReports(puzzleInput).filter(isSafeReport).length.toString();
};

export const partTwo = (puzzleInput: string[]) => {
  const reports = parseReports(puzzleInput);
  let numSafeReports = 0;

  reports.forEach((report) => {
    if (isSafeReport(report)) {
      numSafeReports += 1;
    } else {
      for (let i = 0; i < report.length; i++) {
        const modifiedReport = report.filter((_, index) => index !== i);
        if (isSafeReport(modifiedReport)) {
          numSafeReports += 1;
          break;
        }
      }
    }
  });

  return numSafeReports.toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('02', 'red_nosed_reports', partOne, partTwo, puzzleInput);
}
