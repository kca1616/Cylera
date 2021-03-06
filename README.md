# Cylera Backend Assignment

## The Situation

Imagine there’s a store that handles the checkout automatically for shoppers. As shoppers browse, they can pick out what they like from the shelves. When they select something, a store employee brings that item to the checkout registers. There are many registers (to handle busy shopping times), and the employee must figure out which register to bring the item to. Luckily, the store has built a helper for this exact situation - CheckoutBot - that scans the item and tells the employee which register to take it to.

## The problem

When CheckoutBot scans the item, it knows which shopper selected the item. It then has to decide where to send the employee. CheckoutBot’s goal is to evenly distribute the items between all the registers so that we’re taking full advantage of our resources. However, while attempting to spread the workload, it must also ensure that all items from a single shopper go to the same register, so that the shopper can pick up all their items from a single location when they’re ready to checkout.

Additionally, you must handle the scenario where a shopper checks out and their items are removed from the register they used.

## Hints

- Your solution must interface with the provided Flask API. The API has endpoints for getting the current register states, adding an item, checking out a customer, and clearing the register states.
- The base model is provided to help you get started. You do not have to use it if you prefer not to. You may also change the provided Flask API as long as your implementation serves the same endpoints.
- We have provided a script that generates events, posts the events to your local API, and prints a representation of the register states. You may inspect and run this script when testing your model. Do not edit the event generator script; we will not use any changes you make when we evaluate your model.
- Your solution should be horizontally scalable, in that it should be able to handle many simultaneous requests from different employees trying to sort their shoppers’ items.
- You can assume there are 25 registers.

## Scoring Criteria

- Code quality
- Successful implementation
- Performance
- Distribution of items
