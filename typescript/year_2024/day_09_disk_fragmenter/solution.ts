import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Coord } from '../../utils/grid';
import { delay } from '../../utils/time';

export type FileBlock = { id: number; range: [number, number] };

const formatInput = (puzzleInput: string[]) => {
  const blocks: FileBlock[] = [];
  let currentIndex = 0;

  puzzleInput[0].split('').forEach((val, index) => {
    if (index % 2 === 0) {
      blocks.push({ id: index / 2, range: [currentIndex, currentIndex + Number(val) - 1] });
    }
    currentIndex += Number(val);
  });
  return blocks;
};

const shuffle = (blocks: FileBlock[]) => {
  let i = 0;

  while (i < blocks.length - 2) {
    const b1 = blocks[i];
    const b2 = blocks[i + 1];

    console.log('b1', b1);
    console.log('b2', b2);

    let gapLength = b2.range[0] - b1.range[1] - 1;
    let gapLocation = b1.range[1] + 1;
    let newBlockPos = i + 1;

    while (gapLength != 0) {
      const lastBlock = blocks.at(-1);
      if (!lastBlock) throw new Error('no final element found');

      const lastBlockLength = lastBlock.range[1] - lastBlock.range[0] + 1;

      let newBlock;

      if (lastBlockLength > gapLength) {
        // last block bigger than the gap, will remain in the list
        newBlock = { id: lastBlock.id, range: [gapLocation, gapLocation + gapLength - 1] as Coord };
        console.log([lastBlock.range[0], lastBlock.range[1] - gapLength]);
        lastBlock.range = [lastBlock.range[0], lastBlock.range[1] - gapLength];
        gapLength = 0;
      } else {
        // last block smaller than the gap, will be removed
        newBlock = { id: lastBlock.id, range: [gapLocation, gapLocation + lastBlockLength - 1] as Coord };
        gapLength -= lastBlockLength;
        gapLocation += lastBlockLength;
        blocks.pop();
      }

      console.log('new block pos', newBlockPos);
      console.log('new block', newBlock);
      blocks.splice(newBlockPos, 0, newBlock);
      newBlockPos++;
      console.log(blocks);
    }
    i += gapLength === 0 ? 1 : 2;
  }

  const last = blocks.at(-1);
  const last_2 = blocks.at(-2);
  if (!last || !last_2) throw new Error("Can't find final 2 elements");

  console.log('last', last);
  console.log('last2', last_2);

  last.range = [last_2.range[1] + 1, last_2.range[1] + last.range[1] - last.range[0] + 1];
  console.log('last', last);

  return blocks;
};

export const partOne = async (puzzleInput: string[]) => {
  const formatted = formatInput(puzzleInput);
  const blocks = shuffle(formatted);
  console.log('blocks', blocks);

  console.log(blocks.map((b) => b.id.toString().repeat(b.range[1] - b.range[0] + 1)).join(''));

  return 'Part 1 Answer';
};

export const partTwo = (puzzleInput: string[]) => {
  return 'Part 2 Answer';
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('09', 'disk_fragmenter', partOne, partTwo, puzzleInput);
}
