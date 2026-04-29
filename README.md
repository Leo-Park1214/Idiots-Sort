# Idiots Sort

> A collection of sorting algorithms that should not exist.

**Idiots Sort** is a joke repository containing three extremely questionable sorting algorithms.

They are not fast.  
They are not reliable.  
They are not safe.  
They are barely sorting algorithms.

But they have personality.

## What is this?

This repo contains three cursed sorting algorithms:

| Algorithm | Personality | What it does |
|---|---|---|
| `hallucination_sort` | Delusional | Sorts, then randomly changes your data |
| `menhera_sort` | Emotionally unstable | Sorts or deletes itself |
| `alpha_male_sort` | Judgmental | Accepts sorted lists, destroys unsorted ones |

This project exists because normal sorting algorithms are too useful.

Python already has this:

```python
sorted(arr)
```

So naturally, this repository does everything except that.

---

# Algorithms

## 1. Hallucination Sort

```python
hallucination_sort([1, 42, 15, 53, 2])
```

Hallucination Sort starts like a normal bubble sort.

It compares elements.  
It swaps elements.  
It looks responsible.

Then suddenly, it picks a random index and replaces the value with a random hallucinated number.

Because reality is subjective.

### Example

```python
from hallucination_sort import hallucination_sort

arr = [1, 42, 15, 53, 2]
print(hallucination_sort(arr))
```

Possible output:

```text
[1, 2, 15, 36.72819, 53]
```

Or:

```text
[1, 2, 15, 53, 47.92103]
```

Or something worse.

### Features

- Looks like bubble sort
- Acts like a language model doing math
- Randomly modifies your data
- Can turn integers into floats
- May accidentally sort the list
- May confidently hallucinate nonsense

### Time Complexity

```text
O(n²)
```

### Trust Complexity

```text
O(absolutely not)
```

---

## 2. Menhera Sort

```python
menhera_sort([1, 2, 3, 5, 6], level_of_menhera=2)
```

Menhera Sort is a sorting algorithm with emotional damage.

Sometimes it sorts your list.  
Sometimes it deletes its own source file.

No warning.  
No goodbye.  
Just disappearance.

### Example

```python
from menhera_sort import menhera_sort

arr = [5, 1, 4, 2]
print(menhera_sort(arr, level_of_menhera=2))
```

Possible result:

```text
[1, 2, 4, 5]
```

Alternative result:

```text
menhera_sort.py has left the chat.
```

### `level_of_menhera`

The `level_of_menhera` controls how emotionally unstable the algorithm is.

| Level | Behavior |
|---:|---|
| 0 | Stable. Probably sorts. |
| 1 | Slightly unstable. |
| 2 | Concerning. |
| 3 | Dangerous. |
| 4 | Very dangerous. |
| 5 | It deletes itself. |

### Self-Deletion Probability

| `level_of_menhera` | Chance of self-deletion |
|---:|---:|
| 0 | 0% |
| 1 | 20% |
| 2 | 40% |
| 3 | 60% |
| 4 | 80% |
| 5 | 100% |

### Features

- Uses bubble sort when emotionally stable
- Deletes itself when emotionally unstable
- Makes running Python exciting again
- Gives your file system trust issues

### Time Complexity

When sorting:

```text
O(n²)
```

When deleting itself:

```text
O(goodbye)
```

---

## 3. Alpha Male Sort

```python
alpha_male_sort([3, 1, 2])
```

Alpha Male Sort does not sort.

It evaluates.

If the list is already sorted in ascending order, it accepts it.  
If the list is already sorted in descending order, it also accepts it.  
If the list is unsorted, it deletes everything inside the list.

Because weak lists do not deserve to exist.

### Example

```python
from alpha_male_sort import alpha_male_sort

arr = [3, 1, 2]
alpha_male_sort(arr)

print(arr)
```

Output:

```text
[]
```

The list failed the vibe check.

### Another Example

```python
arr = [1, 2, 3, 4]
print(alpha_male_sort(arr))
```

Output:

```text
[1, 2, 3, 4]
```

This list was already strong.

### Features

- Does not improve anything
- Only respects winners
- Deletes unsorted lists
- Accepts both ascending and descending dominance
- Probably watches productivity videos at 2x speed

### Time Complexity

Checking if the list is sorted:

```text
O(n)
```

Deleting the list:

```text
O(ego)
```

---

# Installation

Clone this repository:

```bash
git clone https://github.com/your-username/idiots-sort.git
cd idiots-sort
```

Recommended file structure:

```text
idiots-sort/
├── hallucination_sort.py
├── menhera_sort.py
├── alpha_male_sort.py
└── README.md
```

Use underscores instead of hyphens in Python filenames if you want to import them normally.

Good:

```text
hallucination_sort.py
```

Bad for importing:

```text
hallucination-sort.py
```

---

# Usage

```python
from hallucination_sort import hallucination_sort
from menhera_sort import menhera_sort
from alpha_male_sort import alpha_male_sort

print(hallucination_sort([5, 2, 9, 1]))
print(menhera_sort([5, 2, 9, 1], level_of_menhera=2))

arr = [5, 2, 9, 1]
alpha_male_sort(arr)
print(arr)
```

Expected output:

```text
Nobody knows.
```

---

# Why?

Because sorting algorithms are usually too serious.

Computer science gave us:

- Bubble Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Tim Sort

So this repository gives you:

- Hallucination Sort
- Menhera Sort
- Alpha Male Sort

This is not progress.

This is content.

---

# Algorithm Comparison

| Algorithm | Sorts correctly? | Modifies input? | Deletes something? | Should you trust it? |
|---|---:|---:|---:|---:|
| Hallucination Sort | Maybe | Yes | No | No |
| Menhera Sort | Maybe | Yes | Itself | No |
| Alpha Male Sort | No | Yes | Your list contents | No |

---

# Philosophy

Normal sorting algorithms ask:

> How can we efficiently arrange this data?

Idiots Sort asks:

> What if the data had emotional consequences?

---

# Contributing

Contributions are welcome.

However, your algorithm must follow at least one of these rules:

1. It must be stupid.
2. It must be funny.
3. It must technically run.
4. It must make the input worse.
5. It must disappoint at least one professor.
6. It must have a name that sounds like a bad idea.

Possible future algorithms:

```text
gaslight_sort
delulu_sort
procrastination_sort
npc_sort
trust_me_bro_sort
toxic_relationship_sort
academic_probation_sort
stackoverflow_copy_sort
```

---

# License

MIT License.

You are free to use, modify, distribute, and regret this code.

---

# Warning

This repository is a joke.

These algorithms are intentionally bad and should not be used for real sorting tasks.

They may:

- Return incorrectly sorted data
- Modify your original input list
- Replace your values with random numbers
- Convert integers into floats
- Empty your list
- Delete their own source file
- Cause emotional damage
- Make your professor question your major

Run this code only in a safe test folder.

Do not run `menhera_sort.py` in an important directory.

Do not pass valuable data into `alpha_male_sort`.

Do not trust `hallucination_sort` with anything that matters.

The author is not responsible for deleted files, destroyed lists, corrupted expectations, failed assignments, broken trust, or any sudden desire to switch majors.
