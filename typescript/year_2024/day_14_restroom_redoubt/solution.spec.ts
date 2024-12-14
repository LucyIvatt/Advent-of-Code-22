import path from "path";
import { InputFile, readPuzzleInput } from "../../utils/readFile";
import { partOne, partTwo } from "./solution";

describe("TestDay14", () => {
  const exampleInput = readPuzzleInput(
    path.resolve(__dirname, InputFile.EXAMPLE),
  );
  const input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));

  describe("Part one", () => {
    it("should return correct answer for the example input", () => {
      const result = partOne(exampleInput);
      expect(result).toBe("Part 1 Answer");
    });

    it("should return correct answer for the real input", () => {
      const result = partOne(input);
      expect(result).toBe("Part 1 Answer");
    });
  });

  describe("Part two", () => {
    it("should return correct answer for the example input", () => {
      const result = partTwo(exampleInput);
      expect(result).toBe("Part 2 Answer");
    });

    it("should return correct answer for the real input", () => {
      const result = partTwo(input);
      expect(result).toBe("Part 2 Answer");
    });
  });
});
