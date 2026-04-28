type Status = "open" | "closed";

type UserProfile = {
  username: string;
  age: number;
  isAdmin: boolean;
};

type Product = {
  name: string;
  price: number;
};

// 1. Create a variable called `courseName` and give it the type `string`.
//    Set it to "TypeScript Basics".

let courseName: string = "TypeScript Basics";

// 2. Create a variable called `hoursStudied` and give it the type `number`.
//    Set it to 2.

let hoursStudied: number = 2;

// 3. Create a variable called `isReady` and give it the type `boolean`.
//    Set it to false.

let isReady: boolean = false;

// 4. Create a variable called `scores` with the type `number[]`.
//    Use at least three numbers.

let scores: number[] = [99, 93, 88];

// 5. Create a variable called `profile` with the type `UserProfile`.
//    Use your own sample data.

let profile: UserProfile = {
  username: "Ruitao",
  age: 24,
  isAdmin: true,
};

// 6. Create a variable called `currentStatus` with the type `Status`.
//    Set it to either "open" or "closed".

let currentStatus: Status = "open";

// 7. Write a function called `add` that takes two numbers and returns a number.

function add(x: number, y: number) {
  return x + y;
}

// 8. Write a function called `formatUser` that takes a `UserProfile`
//    and returns a string like "rita (admin)" or "rita (user)".

function formatUser(profile: UserProfile) {
  return `${profile.username} ${profile.isAdmin ? "admin" : "user"}`;
}

// 9. Write a function called `totalPrice` that takes an array of `Product`
//    and returns the sum of all prices.

function totalPrice(products: Product[]) {
  let sum: number = 0;

  for (const product of products) {
    sum += product.price;
  }

  return sum;
}

// 10. Write a function called `printId` that accepts `string | number`.
//     If it is a string, return it in uppercase.
//     If it is a number, return `ID-<number>`.

function printId(id: string | number) {
  if (typeof id === "string") {
    return id.toUpperCase();
  } else {
    return `ID-${id}`;
  }
}

// 11. Write a function called `getStatusMessage` that accepts `Status`
//     and returns:
//     - "Task is still open" for "open"
//     - "Task is done" for "closed"

function getStatusMessage(status: Status) {
  return `${status === "open" ? "Task is still open" : "Task is done"}`;
}

// 12. Create a `products` array using the `Product[]` type and test `totalPrice`.

let products: Product[] = [
  { name: "Notebook", price: 5 },
  { name: "Pen", price: 2 },
  { name: "Backpack", price: 30 },
];

let result = totalPrice(products);
console.log(result);

// 13. Create a `mixedIds` array with values that are either strings or numbers.
//     Loop through it and call `printId` on each value.

let mixedIds: (string | number)[] = ["fun", 323, "yay", 48];

for (const id of mixedIds) {
  let ids = printId(id);
  console.log(ids);
}

// 14. Extra challenge:
//     Write a function called `describeValue` that accepts `unknown`.
//     Return:
//     - "string: <value>" if the input is a string
//     - "number: <value>" if the input is a number
//     - "boolean: <value>" if the input is a boolean
//     - "unsupported type" for everything else
