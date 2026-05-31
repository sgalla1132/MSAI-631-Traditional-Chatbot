{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "95492396-e000-4988-8615-fbee084f42a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: transformers in c:\\users\\sruth\\anaconda3\\lib\\site-packages (5.9.0)\n",
      "Requirement already satisfied: torch in c:\\users\\sruth\\anaconda3\\lib\\site-packages (2.12.0)\n",
      "Requirement already satisfied: huggingface-hub<2.0,>=1.5.0 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from transformers) (1.17.0)\n",
      "Requirement already satisfied: numpy>=1.17 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from transformers) (1.26.4)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from transformers) (25.0)\n",
      "Requirement already satisfied: pyyaml>=5.1 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from transformers) (6.0.1)\n",
      "Requirement already satisfied: regex>=2025.10.22 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from transformers) (2026.5.9)\n",
      "Requirement already satisfied: tokenizers<=0.23.0,>=0.22.0 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from transformers) (0.22.2)\n",
      "Requirement already satisfied: typer in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from transformers) (0.25.1)\n",
      "Requirement already satisfied: safetensors>=0.4.3 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from transformers) (0.7.0)\n",
      "Requirement already satisfied: tqdm>=4.27 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from transformers) (4.66.5)\n",
      "Requirement already satisfied: filelock in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from torch) (3.13.1)\n",
      "Requirement already satisfied: typing-extensions>=4.10.0 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from torch) (4.11.0)\n",
      "Requirement already satisfied: setuptools<82 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from torch) (75.1.0)\n",
      "Requirement already satisfied: sympy>=1.13.3 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from torch) (1.14.0)\n",
      "Requirement already satisfied: networkx>=2.5.1 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from torch) (3.5)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from torch) (3.1.4)\n",
      "Requirement already satisfied: fsspec>=0.8.5 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from torch) (2024.6.1)\n",
      "Requirement already satisfied: click>=8.4.0 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (8.4.1)\n",
      "Requirement already satisfied: hf-xet<2.0.0,>=1.4.3 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (1.5.0)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (0.27.0)\n",
      "Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from sympy>=1.13.3->torch) (1.3.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from tqdm>=4.27->transformers) (0.4.6)\n",
      "Requirement already satisfied: shellingham>=1.3.0 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from typer->transformers) (1.5.0)\n",
      "Requirement already satisfied: rich>=13.8.0 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from typer->transformers) (15.0.0)\n",
      "Requirement already satisfied: annotated-doc>=0.0.2 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from typer->transformers) (0.0.4)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from jinja2->torch) (2.1.3)\n",
      "Requirement already satisfied: anyio in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (4.2.0)\n",
      "Requirement already satisfied: certifi in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (2025.6.15)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (1.0.2)\n",
      "Requirement already satisfied: idna in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (3.7)\n",
      "Requirement already satisfied: sniffio in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (1.3.0)\n",
      "Requirement already satisfied: h11<0.15,>=0.13 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (0.14.0)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from rich>=13.8.0->typer->transformers) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from rich>=13.8.0->typer->transformers) (2.15.1)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\sruth\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich>=13.8.0->typer->transformers) (0.1.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install transformers torch"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e667c5e-fbc1-40e0-9890-fb314a6e2698",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5fdd382723b54da596fb4bfe91d7ffa1",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Loading weights:   0%|          | 0/104 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Campus Helper AI Chatbot\n",
      "Type 'bye', 'exit', or 'quit' to stop.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  hi\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bot: Hello! I am Campus Helper AI. Type 'help' to see what I can do.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  help\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bot: I can help with: assignments, deadlines, instructor info, GitHub/project info, and sentiment analysis. Try typing: sentiment I love this class\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  sentiment I love this class\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bot: The sentiment is POSITIVE with a confidence score of 1.0.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  sentiment This assignment is frustrating\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bot: The sentiment is NEGATIVE with a confidence score of 0.999.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  git\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bot: Sorry, I did not understand that. Type 'help' to see what I can answer.\n"
     ]
    }
   ],
   "source": [
    "from transformers import pipeline\n",
    "\n",
    "sentiment_analyzer = pipeline(\n",
    "    \"sentiment-analysis\",\n",
    "    model=\"distilbert/distilbert-base-uncased-finetuned-sst-2-english\"\n",
    ")\n",
    "\n",
    "def chatbot_response(user_input):\n",
    "    user_input_clean = user_input.lower().strip()\n",
    "\n",
    "    if user_input_clean in [\"hello\", \"hi\", \"hey\"]:\n",
    "        return \"Hello! I am Campus Helper AI. Type 'help' to see what I can do.\"\n",
    "\n",
    "    elif user_input_clean == \"help\":\n",
    "        return (\n",
    "            \"I can help with: assignments, deadlines, instructor info, \"\n",
    "            \"GitHub/project info, and sentiment analysis. \"\n",
    "            \"Try typing: sentiment I love this class\"\n",
    "        )\n",
    "\n",
    "    elif user_input_clean.startswith(\"sentiment\"):\n",
    "        text_to_analyze = user_input.replace(\"sentiment\", \"\", 1).strip()\n",
    "\n",
    "        if text_to_analyze == \"\":\n",
    "            return \"Please type a sentence after the word sentiment. Example: sentiment I love this project\"\n",
    "\n",
    "        result = sentiment_analyzer(text_to_analyze)[0]\n",
    "        label = result[\"label\"]\n",
    "        score = round(result[\"score\"], 3)\n",
    "\n",
    "        return f\"The sentiment is {label} with a confidence score of {score}.\"\n",
    "\n",
    "    elif \"assignment\" in user_input_clean:\n",
    "        return \"This project requires integrating a traditional chatbot with an AI service and documenting the process.\"\n",
    "\n",
    "    elif \"deadline\" in user_input_clean:\n",
    "        return \"Please check the course shell for the official deadline. Most assignments are due by 11:59 PM.\"\n",
    "\n",
    "    elif \"instructor\" in user_input_clean:\n",
    "        return \"Your instructor is Professor Ying Lin. Use the course email or announcements for official contact.\"\n",
    "\n",
    "    elif \"github\" in user_input_clean or \"repo\" in user_input_clean:\n",
    "        return \"You need to upload the source code to GitHub and include the repository URL in the report.\"\n",
    "\n",
    "    elif user_input_clean in [\"bye\", \"exit\", \"quit\"]:\n",
    "        return \"Goodbye! Good luck with your AI chatbot project.\"\n",
    "\n",
    "    else:\n",
    "        return \"Sorry, I did not understand that. Type 'help' to see what I can answer.\"\n",
    "\n",
    "\n",
    "print(\"Campus Helper AI Chatbot\")\n",
    "print(\"Type 'bye', 'exit', or 'quit' to stop.\")\n",
    "\n",
    "while True:\n",
    "    user_input = input(\"You: \")\n",
    "    response = chatbot_response(user_input)\n",
    "    print(\"Bot:\", response)\n",
    "\n",
    "    if user_input.lower().strip() in [\"bye\", \"exit\", \"quit\"]:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0b1c58e-9414-4092-a16a-8ebae3a68918",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
