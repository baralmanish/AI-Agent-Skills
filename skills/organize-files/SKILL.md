---
name: organize-files
description: "Use this skill when the user needs files organized. Triggers on: organize files, reorganize files, sort files, clean up files, file structure, rename files, folder structure, zip files, downloadable archive."
tags: [file-management, organization, productivity, archiving]
argument-hint: "Optional: describe the files to organize and how you want them grouped (e.g., by project, date, topic)"
user-invocable: true
disable-model-invocation: false
---

# Organize Files

## When to Use

- User uploads or references a set of files to organize
- User wants files renamed with a consistent naming scheme
- User needs a logical folder hierarchy created
- User wants a downloadable zip of reorganized files

## Process

### 1. Reflect on the User's Real Goal Before Organizing

Before organizing files, review the full conversation and extract:

- The user's real goal for organization
- Core intent and most important entities
- Main retrieval needs the structure should support

Determine what must be optimized for this collection, such as:

- Fast lookup
- Chronological browsing
- Project tracking
- Client-based access
- Topic grouping
- Document-type separation
- Version clarity
- Archival cleanliness

Translate this into clear priorities:

- What must be obvious from filenames
- What must be obvious from folder structure
- What can remain secondary

### 2. Design the Naming Scheme First

Define naming rules before renaming any files.

- If the user provides a convention, follow it closely and apply it consistently across the full file set.
- If no convention is provided, create one that best supports the organization goal and enables recognition without opening files.
- Preserve key distinctions where relevant: date, project, topic, client, file type, version, and status.
- Ensure names are clean, uniform, readable, sortable, and specific enough to distinguish similar files without unnecessary clutter.

### 3. Design the Folder Hierarchy as a Deliberate Taxonomy

Build an intentional structure, not a loose pile of categories.

- Choose shallow vs. deep hierarchy based on collection size, complexity, and expected future use.
- Use shallow structure when simplicity is best.
- Use multiple levels when deeper grouping improves intuition and reduces clutter.
- Group first by the most meaningful retrieval dimension, then by secondary dimensions.
- Keep related files together, place ambiguous files thoughtfully, and minimize catch-all folders.

### 4. Rename and Reorganize the Files

Execute the reorganization consistently and carefully:

- Apply naming rules to all files
- Move files into the new hierarchy
- Clean vague names, inconsistent formatting, duplicates, and unnecessary noise while preserving important meaning
- Infer categories when needed from filenames, metadata, extensions, contents, or surrounding context

The final system should feel intuitive, legible, and scalable.

### 5. Zip and Deliver

- Package the fully reorganized folder structure into a single downloadable `.zip` archive
- Provide the user with a link to download it

### 6. Explain the Logic Briefly

Provide a concise explanation of:

- The naming scheme used
- The folder hierarchy created
- Important judgment calls for ambiguous files, duplicates, or unusual cases

## Supporting References

This skill includes naming convention and folder taxonomy rules:

- **NAMING_CONVENTIONS.json** — Naming patterns by file type (reports, meeting notes, design files, images, code, data exports, presentations, invoices, versions), date format standards (ISO 8601), naming principles, folder hierarchy patterns (by project, date, type, topic, hybrid), depth rules, and zip output specification. Located in `references/`.

The AI uses NAMING_CONVENTIONS.json to design a consistent naming scheme before renaming any files, ensuring the result is sortable, scannable, and consistent.

## Output

**ALWAYS produce a fully reorganized file collection with renamed files, a clear folder hierarchy, and a downloadable zip archive. Creating the organized structure and returning it as a zip file is the entire purpose of this skill. The user must get a clean, intuitive, ready-to-download result.**

Required response elements:

1. **Renamed files** — all files follow the defined naming scheme
2. **Clear folder hierarchy** — all files are placed in the designed taxonomy
3. **Downloadable zip archive** — complete reorganized structure in one archive, with download link
4. **Brief summary** — naming logic, folder logic, and key judgment calls

## Example Invocations

- "Organize these files based on what they show and what AI skill concept is being demonstrated."
- "I have a messy downloads folder — organize it by file type and date."
- "Reorganize these project files so they make sense to a new team member."
