# Frontend Design — Quick Reference

## Triggers

- "Build a landing page with [aesthetic]"
- "Design a component that looks like [description]"
- "Redesign this UI to be more [adjective]"
- "Create a [type] page with [style] aesthetic"
- "Build a dashboard/form/interface for [purpose]"

## Aesthetic Directions (Pick One)

| Direction      | Use When                    | Key Elements                                 |
| -------------- | --------------------------- | -------------------------------------------- |
| **Minimal**    | Less is more, clean slate   | Whitespace, single color, typography         |
| **Maximalist** | Complex, layered, bold      | Patterns, 3+ colors, texture, complexity     |
| **Luxury**     | Elegant, refined, premium   | Generous spacing, gold/black, subtle details |
| **Playful**    | Fun, approachable, youthful | Bright colors, unusual shapes, personality   |
| **Brutalist**  | Raw, honest, no polish      | Minimal styling, true colors, functional     |
| **Retro**      | Nostalgic with modern twist | Gradients, glitch effects, bold geometry     |

## Design Checklist

- [ ] Unique color palette (3-5 main colors)
- [ ] Distinctive typography (at least 2 typefaces)
- [ ] Clear visual hierarchy
- [ ] Consistent spacing/rhythm
- [ ] Hover/active states planned
- [ ] Mobile responsive approach
- [ ] Accessibility considered (contrast, ARIA)
- [ ] 1-2 key micro-interactions

## Component Quick Build

```
What: [Component name]
Purpose: [Why it exists]
States: [Default, hover, focus, disabled, loading, error]
Colors: [Primary, secondary, accent]
Typography: [Headings, body, labels]
Motion: [Entrance, exit, interaction]
```

## Typography Pairing Quick Reference

| Display Font     | Body Font | Feel              |
| ---------------- | --------- | ----------------- |
| Playfair Display | Inter     | Editorial/Elegant |
| Montserrat       | Open Sans | Modern/Corporate  |
| Bebas Neue       | Roboto    | Bold/Structured   |
| Cormorant        | Lato      | Luxury/Refined    |
| Space Mono       | Nunito    | Tech/Friendly     |
| Bodoni Moda      | Work Sans | Timeless/Bold     |

## Color Psychology Quick Reference

| Color       | Emotion             | Use For                      |
| ----------- | ------------------- | ---------------------------- |
| Blue        | Trust, calm         | Finance, tech, corporate     |
| Green       | Growth, health      | Wellness, environment, money |
| Red         | Urgency, passion    | CTAs, alerts, sales          |
| Purple      | Creativity, luxury  | Design, premium, magic       |
| Orange      | Energy, playful     | Food, startup, fun           |
| Pink        | Soft, playful       | Fashion, lifestyle, modern   |
| Black       | Authority, elegance | Luxury, tech, contrast       |
| White/Cream | Clean, premium      | Minimalist, editorial        |

## Responsive Breakpoints (Common)

```
Mobile:   320px - 639px
Tablet:   640px - 1023px
Desktop:  1024px+
```

## Animation Quick Tips

✨ **High-Impact**: Page loads, hero section, scroll reveals  
⚡ **Subtle**: Hover states, micro-interactions, transitions  
🔄 **Loops**: Only if meaningful (loading spinners, etc.)  
⏱️ **Timing**: 200-500ms for snappy, 800-1200ms for dramatic

## Accessibility Checklist

- [ ] Contrast ratio ≥ 4.5:1 for text
- [ ] Color not only differentiator
- [ ] Keyboard navigation works
- [ ] Focus states visible
- [ ] Alt text for images
- [ ] ARIA labels where needed

## Common Mistakes to Avoid

❌ Using stock photos without context  
❌ Too many fonts (stick to 2-3)  
❌ Inconsistent spacing  
❌ Colors that clash (check accessibility)  
❌ Animations that don't add value  
❌ Ignoring mobile (design mobile-first)  
❌ Inaccessible color contrast  
❌ Unclear visual hierarchy

## File Structure for Deliverables

```
component.html         - Static HTML/CSS version
component.jsx          - React component version
component.vue          - Vue component version
component.module.css   - Scoped styles (if applicable)
assets/               - Images, icons
```

## Code Quality Standards

✅ Semantic HTML  
✅ Mobile-first CSS  
✅ No inline styles (use classes)  
✅ Proper spacing utilities  
✅ Accessible form inputs  
✅ Responsive images  
✅ Clean, readable code
