import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { partOne, partTwo } from './solution';

describe('TestDay17', () => {
  const exampleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  const exampleInput2 = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE_2));
  const input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));

  describe('Part one', () => {
    it('should return correct answer for the example input', () => {
      const result = partOne(exampleInput);
      expect(result).toBe('4,6,3,5,6,3,5,2,1,0');
    });

    it('should return correct answer for the real input', () => {
      const result = partOne(input);
      expect(result).toBe('6,2,7,2,3,1,6,0,5');
    });
  });

  describe('Part two', () => {
    it('should return correct answer for the example input', () => {
      const result = partTwo(exampleInput2);
      expect(result).toBe('117440');
    });

    it('should return correct answer for the real input', () => {
      const result = partTwo(input);
      expect(result).toBe('236548287712877');
    });
  });
});
