# The history of C

```mermaid
timeline
    title History of C
    section History of creation
        1970s : creation of C : by Dennis Ritchie
        1978 : creation of "The C Programming Language" book : by Brian Kernighan and Dennis Ritchie
        1983 : ANSI C : formed a committee to establish a standard specification for the C language.
        1989 : ANSI C (also known as C89 or C90) : Become a widely accepted version of the C language : This standardization made it easier for programmers to write code that worked on different systems.
    section History of updates
        1990s : C99 : new features : inline functions, several new data types
        2007 : C11 : new features : type generic macros, anonymous structures, improved Unicode support, atomic operations, multi-threading, and bounds-checked functions.
        2018 : C17 : current standard for the C programming language : only technical corrections, and clarifications to defects in C11
```

# Origins: 

- Evolved from an earlier language called B, which was created by Ken Thompson.
- Written by Brian Kernighan and Dennis Ritchie in the 1970s
- C is closely tied to the development of the Unix operating system, originally implemented in ***assembly language***

# K&R C:

 The first widely used version of C was documented in "The C Programming Language" book by Brian Kernighan and Dennis Ritchie, published in 1978. This edition of C is often referred to as "K&R C."

# What purpose

### 1. Operating System Development:
    - develop the Unix operating system
    - provide a higher-level, portable language for writing Unix
    - adapted to the operating system to various computer platforms.

### 2. Portability:
    - designed to be a portable language
    - separating the low-level, machine-specific code from the high-level code
    - easier to adapt programs to different systems.

### 3. Efficiency:
    - provide a balance between high-level programming languages and low-level assembly languages
    - allow programmers to write code that was more efficient than many high-level languages while maintaining the readability and ease of use found in those languages.

### 4. Systems Programming:
    - intended to be a language for systems programming
    - its low-level capabilities and direct memory access made it suitable for these usages

### 5. Tool Development:
    - used to create a wide range of system utilities and development tools, such as the C compiler itself (which was initially written in assembly but later rewritten in C)

### 6. General-Purpose Language:
    - initially created for systems programming
    - C's simplicity and power made it a versatile, general-purpose programming language that could be applied to various domains.

In summary, C was created to facilitate the development of Unix and to address the challenges of portability, efficiency, and systems programming. Its success in these areas contributed to its widespread adoption and long-lasting popularity in various programming domains.

---

# Character set

The basic C source character set includes the following characters:

- Lowercase and uppercase letters of ISO Basic Latin Alphabet: a–z A–Z
- Decimal digits: 0–9
- Graphic characters: ! " # % & ' ( ) * + , - . / : ; < = > ? [ \ ] ^ _ { | } ~
- Whitespace characters: space, horizontal tab, vertical tab, form feed, newline