# Daily Reflection Tree - Design Rationale

## Goal

To create a deterministic reflection tool that helps employees think about their day through three psychological lenses:

1. Response and agency
2. Contribution and value given
3. Perspective beyond self

## Why These Questions

I chose realistic workplace moments such as stress, recognition, helping others, and handling pressure because users can relate to them easily after a workday.

## Branching Logic

The tree uses fixed multiple-choice options only.

Different answers lead to different reflections:

- difficult day vs steady day
- contribution vs appreciation focus
- self-focus vs wider perspective

This keeps the experience deterministic and auditable.

## Psychological Basis

The design is inspired by:

- Locus of Control
- Growth Mindset
- Contribution Orientation
- Perspective Taking

## Why No Runtime AI

The system uses predefined logic and text. This avoids hallucination, keeps responses consistent, and builds trust.

## Improvements With More Time

- deeper branching
- personalized summaries using state tallies
- web interface dashboard
- progress tracking over time