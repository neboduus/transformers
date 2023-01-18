from datasets import load_dataset, concatenate_datasets, DatasetDict
from transformers import AutoTokenizer


def show_samples(dataset, num_samples=3, seed=42):
    sample = dataset["train"].shuffle(seed=seed).select(range(num_samples))
    for example in sample:
        print(f"\n'>> Title: {example['review_title']}'")
        print(f"'>> Review: {example['review_body']}'")


def filter_books(example):
    return (
        example["product_category"] == "book"
        or example["product_category"] == "digital_ebook_purchase"
    )


spanish_dataset = load_dataset('amazon_reviews_multi', 'es')
english_dataset = load_dataset('amazon_reviews_multi', 'en')

print('\nEnglish Dataset:\n')
print(english_dataset)

show_samples(english_dataset)

english_dataset.set_format("pandas")
english_df = english_dataset["train"][:]

print('\nCounts for top 20 products:\n')
print(english_df["product_category"].value_counts()[:20])

english_dataset.reset_format()

spanish_books = spanish_dataset.filter(filter_books)
english_books = english_dataset.filter(filter_books)
show_samples(english_books)

books_dataset = DatasetDict()

for split in english_books.keys():
    books_dataset[split] = concatenate_datasets(
        [english_books[split], spanish_books[split]]
    )
    books_dataset[split] = books_dataset[split].shuffle(seed=42)

# Peek at a few examples
show_samples(books_dataset)

books_dataset = books_dataset\
    .filter(lambda x: len(x["review_title"].split()) > 2)

model_checkpoint = "google/mt5-small"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

inputs = tokenizer("I loved reading the Hunger Games!")
print('\nInputs:\n')
print(inputs)



