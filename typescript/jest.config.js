/** @type {import('ts-jest').JestConfigWithTsJest} **/
export const testEnvironment = "node";
export const transform = {
  "^.+.tsx?$": ["ts-jest", {}],
};
export default {
  testEnvironment: "node",
  transform: {
    "^.+.tsx?$": ["ts-jest", {}],
  },
  testPathIgnorePatterns: [".d.ts", ".js"],
};
