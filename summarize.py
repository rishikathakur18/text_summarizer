import click
from transformers import pipeline

summarizer = pipeline("summarization")

@click.command()
@click.option('-t', '--text', help='Text or path to text file to summarize')
def summarize(text):
    if text.endswith('.txt'):
        try:
            with open(text, 'r', encoding='utf-8') as file:
                text = file.read()
        except Exception as e:
            click.echo(f"Error reading file: {e}")
            return
    
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    click.echo("Summary:\n" + summary[0]['summary_text'])

if __name__ == '__main__':
    summarize()
