# TypeScript Learning Roadmap

## Goal

Use this folder as a hands-on place to learn TypeScript by writing small programs, checking types often, and gradually building toward small projects.

## Core Approach

1. Learn one idea at a time.
2. Write a short exercise for that idea immediately.
3. Run `tsc --noEmit <file>` to check types.
4. Write a short note about what was confusing.
5. Revisit older exercises and improve the types.

## Phase 1: Setup and Mental Model

### Why it matters

TypeScript is JavaScript plus a type system. The first job is understanding what TypeScript checks before the code runs.

### Learn

- What TypeScript is and is not
- Type checking vs runtime behavior
- How to use `tsc`
- Why strict typing is useful

### Practice

- Run `tsc --version`
- Create a `.ts` file and check it with `tsc --noEmit`
- Intentionally create one type error and read the compiler message

### Done when

- You can explain what TypeScript catches before runtime
- You can run the compiler on a single file without help

## Phase 2: Basic Types and Values

### Why it matters

These are the building blocks for everything else.

### Learn

- `string`, `number`, `boolean`
- Arrays
- Object literals
- Explicit types vs inferred types
- Literal types
- Union types

### Practice

- Type a user profile object
- Type a list of scores
- Make a variable that can hold either `"open"` or `"closed"`
- Fix a few deliberate mismatched assignments

### Done when

- You can type simple variables, arrays, and objects without guessing
- You understand when TypeScript infers the type and when to write it yourself

## Phase 3: Functions

### Why it matters

Functions are where types start becoming useful instead of decorative.

### Learn

- Parameter types
- Return types
- Optional parameters
- Default values
- Function type signatures

### Practice

- Write a function that formats a username
- Write a function that adds numbers from an array
- Write a function with an optional label
- Write a function that returns either a string or number depending on input rules

### Done when

- You can type normal utility functions confidently
- You can spot missing return types and incorrect argument usage

## Phase 4: Reusable Shapes

### Why it matters

Real code repeats data shapes. Reusable types keep that code readable.

### Learn

- Type aliases
- Interfaces
- Nested objects
- Readonly properties
- Optional object properties

### Practice

- Model a `Task`
- Model a `Student`
- Compare `type` and `interface` on simple examples
- Create a nested settings object

### Done when

- You know when to extract a repeated object shape
- You can read and write basic custom types quickly

## Phase 5: Narrowing and Safe Unknown Data

### Why it matters

TypeScript becomes powerful when values can have more than one possible shape.

### Learn

- Narrowing with `typeof`
- Narrowing with `in`
- Truthy and falsy checks
- `unknown` vs `any`
- `never` at a basic level

### Practice

- Accept `string | number` and handle both safely
- Parse unknown input into a known object shape
- Replace unsafe `any` with `unknown` plus checks

### Done when

- You stop guessing and start proving types through checks
- You understand why `unknown` is safer than `any`

## Phase 6: Collections and Data Modeling

### Why it matters

Most applications work with lists of structured data.

### Learn

- Arrays of objects
- Simple records and dictionaries
- Transforming arrays with typed callbacks
- Basic data modeling choices

### Practice

- Create a task list
- Filter completed items
- Group values by category
- Build a small gradebook data model

### Done when

- You can model small real-world datasets without collapsing into `any`

## Phase 7: Generics

### Why it matters

Generics let you write reusable code without losing type information.

### Learn

- Generic functions
- Generic arrays and objects
- Type parameters
- Constraints with `extends`

### Practice

- Write an identity function
- Write a function that returns the first item in an array
- Write a helper that extracts one property from an object safely

### Done when

- You understand how generics preserve relationships between input and output

## Phase 8: Utility Types and Type Transformations

### Why it matters

You often need to derive new types from existing ones.

### Learn

- `Partial`
- `Required`
- `Pick`
- `Omit`
- `Record`

### Practice

- Create an update type for a `Task`
- Build a category map with `Record`
- Create a public version of a larger object with `Pick` or `Omit`

### Done when

- You can reshape an existing type without redefining everything

## Phase 9: Classes and Object-Oriented Features

### Why it matters

Even if you do not prefer classes, you need to be able to read them.

### Learn

- Class properties
- Constructors
- Access modifiers
- Methods
- Implementing interfaces

### Practice

- Create a `BankAccount` class
- Create a `StudentRecord` class
- Implement a simple interface in a class

### Done when

- You can read and write straightforward class-based code

## Phase 10: Modules and Project Structure

### Why it matters

Once code grows, file boundaries matter.

### Learn

- `export` and `import`
- Named vs default exports
- Splitting types and logic across files

### Practice

- Move a shared `Task` type into its own file
- Import helper functions into a second exercise file

### Done when

- You can organize a tiny multi-file TypeScript project cleanly

## Phase 11: Compiler Configuration

### Why it matters

`tsconfig.json` controls how strict and useful TypeScript will be.

### Learn

- What `tsconfig.json` does
- `strict`
- `noEmit`
- `target`
- `module`

### Practice

- Create a minimal `tsconfig.json`
- Turn on strict mode
- Observe how stricter settings change your errors

### Done when

- You can explain why strict mode is worth the friction

## Phase 12: Async Code and APIs

### Why it matters

Real programs fetch data and wait for work to finish.

### Learn

- `Promise`
- `async` and `await`
- Typing resolved values
- Typing API-like response shapes

### Practice

- Mock a fetch response type
- Write an async function that returns typed data
- Handle success and failure shapes

### Done when

- You can type a basic async workflow without falling back to `any`

## Phase 13: Environment-Specific Typing

### Why it matters

TypeScript feels different in Node and the browser.

### Learn

- Basic Node types
- Basic DOM types
- Event typing

### Practice

- Node option: read and transform data in a script
- Browser option: type a form submit handler

### Done when

- You can choose the right environment types for a small exercise

## Phase 14: Practical Patterns

### Why it matters

This is where the language starts feeling useful in normal programs.

### Learn

- Config objects
- Validation patterns
- Discriminated unions
- State-like object shapes

### Practice

- Create a typed app config object
- Build a result type for success or failure
- Model an order or task state machine

### Done when

- You can use types to make invalid states harder to represent

## Phase 15: Capstones and Review

### Why it matters

Learning sticks when multiple ideas are combined.

### Practice

- Mini project: task manager
- Mini project: inventory tracker
- Mini project: grade calculator
- Mini project: API response formatter

### Review checklist

- Can I model data clearly?
- Can I write typed functions confidently?
- Can I narrow union types safely?
- Can I avoid `any` most of the time?
- Can I read compiler errors without panicking?

### Done when

- You can build small TypeScript programs without copying patterns blindly

## First Exercises

Start with `exercises/01-foundations.ts`.

Goals for this first batch:

- typed variables
- typed arrays
- typed objects
- typed functions
- simple unions
- basic narrowing

Suggested workflow:

1. Open the exercise file.
2. Fill in the missing types and implementations.
3. Run `tsc --noEmit exercises/01-foundations.ts`.
4. Fix errors until the file type-checks.
5. Add one or two notes below about what was hardest.
