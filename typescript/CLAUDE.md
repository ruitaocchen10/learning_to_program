# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

A hands-on TypeScript learning workspace. The user works through exercises one concept at a time, checks types with the compiler, and takes notes on what was confusing. This file is a memory for the agent which informs it on the current state of the user's progress

## Workflow

Per `roadmap.md`, the intended loop for each exercise is:

1. Fill in missing types/implementations in the exercise file
2. Run `tsc --noEmit` on the file
3. Fix errors until it type-checks clean

## Tutoring style

The user is learning by doing and prefers to be guided with questions and hints rather than given complete solutions. When helping with exercises, ask leading questions and point toward the right idea — don't write the answer outright.

## Progress

Currently working through **Phase 5 (Narrowing)**. Comfortable with basic types, typed functions, type aliases, and `typeof` narrowing. Has not yet worked with `unknown` or generics.
