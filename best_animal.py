import random


class TreeNode:
  """A node representing an element in the Binary Search Tree."""

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class AnimalTree:
  """A Binary Search Tree for storing and organizing animal names alphabetically."""

  def __init__(self):
    self.root = None

  def insert(self, value):
    if not self.root:
      self.root = TreeNode(value)
    else:
      self._insert_recursive(self.root, value)

  def _insert_recursive(self, node, value):
    if value < node.value:
      if node.left is None:
        node.left = TreeNode(value)
      else:
        self._insert_recursive(node.left, value)
    elif value > node.value:
      if node.right is None:
        node.right = TreeNode(value)
      else:
        self._insert_recursive(node.right, value)

  def to_list(self):
    """Performs an in-order traversal to return all animals as a sorted list."""
    elements = []
    self._inorder_traversal(self.root, elements)
    return elements

  def _inorder_traversal(self, node, elements):
    if node:
      self._inorder_traversal(node.left, elements)
      elements.append(node.value)
      self._inorder_traversal(node.right, elements)


# List of ~200 animals strictly excluding all felines (cats, tigers, lions, etc.)
animals_data = [
    # Mammals (Canids, Ursids, Ungulates, Marsupials, etc.)
    "Dog",
    "Wolf",
    "Fox",
    "Coyote",
    "Jackal",
    "Dingo",
    "Bear",
    "Grizzly Bear",
    "Polar Bear",
    "Panda",
    "Red Panda",
    "Raccoon",
    "Skunk",
    "Badger",
    "Otter",
    "Weasel",
    "Ferret",
    "Mink",
    "Wolverine",
    "Elephant",
    "African Elephant",
    "Asian Elephant",
    "Hippopotamus",
    "Rhinoceros",
    "Tapir",
    "Horse",
    "Donkey",
    "Mule",
    "Zebra",
    "Giraffe",
    "Camel",
    "Dromedary",
    "Llama",
    "Alpaca",
    "Vicuna",
    "Guanaco",
    "Deer",
    "Elk",
    "Moose",
    "Caribou",
    "Reindeer",
    "Antelope",
    "Gazelle",
    "Bison",
    "Buffalo",
    "Cow",
    "Sheep",
    "Goat",
    "Pig",
    "Boar",
    "Warthog",
    "Kangaroo",
    "Koala",
    "Wombat",
    "Tasmanian Devil",
    "Platypus",
    "Echidna",
    "Opossum",
    "Quokka",
    "Sugar Glider",
    "Sloth",
    "Armadillo",
    "Anteater",
    "Pangolin",
    "Hedgehog",
    "Porcupine",
    "Beaver",
    "Rabbit",
    "Hare",
    "Chipmunk",
    "Squirrel",
    "Gopher",
    "Groundhog",
    "Mole",
    "Shrew",
    "Bat",
    "Vampire Bat",
    "Fruit Bat",
    "Dolphin",
    "Porpoise",
    "Whale",
    "Blue Whale",
    "Humpback Whale",
    "Killer Whale",
    "Sperm Whale",
    "Narwhal",
    "Beluga Whale",
    "Manatee",
    "Dugong",
    "Seal",
    "Sea Lion",
    "Walrus",
    "Chimpanzee",
    "Gorilla",
    "Orangutan",
    "Baboon",
    "Lemur",
    "Macaque",
    "Gibbon",
    # Birds
    "Eagle",
    "Bald Eagle",
    "Hawk",
    "Falcon",
    "Owl",
    "Barn Owl",
    "Snowy Owl",
    "Crow",
    "Raven",
    "Blue Jay",
    "Cardinal",
    "Sparrow",
    "Pigeon",
    "Dove",
    "Seagull",
    "Pelican",
    "Albatross",
    "Penguin",
    "Emperor Penguin",
    "Ostrich",
    "Emu",
    "Cassowary",
    "Kiwi",
    "Flamingo",
    "Heron",
    "Egret",
    "Stork",
    "Swan",
    "Goose",
    "Duck",
    "Turkey",
    "Chicken",
    "Rooster",
    "Peacock",
    "Pheasant",
    "Quail",
    "Parrot",
    "Macaw",
    "Cockatoo",
    "Toucan",
    "Woodpecker",
    "Hummingbird",
    "Robin",
    "Swallow",
    "Canary",
    "Finch",
    "Magpie",
    "Vulture",
    "Condor",
    # Reptiles & Amphibians
    "Crocodile",
    "Alligator",
    "Caiman",
    "Iguana",
    "Chameleon",
    "Gecko",
    "Komodo Dragon",
    "Python",
    "Boa Constrictor",
    "Anaconda",
    "Rattlesnake",
    "Viper",
    "Cobra",
    "Tortoise",
    "Sea Turtle",
    "Box Turtle",
    "Frog",
    "Tree Frog",
    "Bullfrog",
    "Toad",
    "Salamander",
    "Newt",
    "Axolotl",
    # Fish & Marine Life
    "Great White Shark",
    "Hammerhead Shark",
    "Tiger Shark",  # (Shark, not feline cat)
    "Stingray",
    "Manta Ray",
    "Salmon",
    "Tuna",
    "Trout",
    "Goldfish",
    "Clownfish",
    "Pufferfish",
    "Swordfish",
    "Eel",
    "Barracuda",
    "Jellyfish",
    "Octopus",
    "Squid",
    "Cuttlefish",
    "Crab",
    "Lobster",
    "Shrimp",
    "Starfish",
    "Sea Urchin",
    "Sea Anemone",
    # Insects & Invertebrates
    "Butterfly",
    "Monarch Butterfly",
    "Moth",
    "Bee",
    "Wasp",
    "Ant",
    "Beetle",
    "Ladybug",
    "Dragonfly",
    "Damselfly",
    "Grasshopper",
    "Cricket",
    "Praying Mantis",
    "Cicada",
    "Firefly",
    "Centipede",
    "Millipede",
    "Snail",
    "Slug",
    "Earthworm",
    "Scorpion",
    "Tarantula",
    "Spider",
]


def main():
  # Initialize the Binary Search Tree
  bst = AnimalTree()

  # Insert each animal into the tree
  for animal in animals_data:
    bst.insert(animal)

  # Retrieve all elements back from the tree structure
  stored_animals = bst.to_list()

  # Randomly pick and display one animal
  selected_animal = random.choice(stored_animals)

  #print(f"Total animals stored in tree: {len(stored_animals)}")
  print(f"Sabrina's best animal ever: {selected_animal} (Never a cat!)")


if __name__ == "__main__":
  main()
  input("\nPress Enter to exit...") # Pause for all dwell in 'fact'
