# Open Source Quantized LLMs Independent Assessment Repository

## Introduction

Welcome to our Open Source Quantized Large Language Models (LLMs) Independent Assessment repository. This repository aims to benchmark and provide a comprehensive, independent assessment of quantized versions of open source Large Language Models. It strives to offer an unbiased and transparent picture of the performance trade-offs of these quantized LLMs.

## Background

Large Language Models have achieved breakthrough results across a variety of Natural Language Processing tasks, and their utility continues to expand across multiple disciplines. However, the deployment of such models is often constrained by their size and computational requirements, prompting researchers to explore model quantization as a viable solution.

Quantization refers to the process of reducing the precision of the weights in a neural network model. This reduction in precision can help decrease the computational and memory requirements of the models, enabling their deployment in resource-constrained environments such as mobile devices and edge devices. However, the quantization process often leads to a degradation in the model's performance. Understanding this trade-off between computational efficiency and model performance is crucial for the practical deployment of these models.

Although the [Open Source LLM leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) has been instrumental in providing benchmarking results for different LLMs, it currently does not include assessments of quantized versions of these models. This omission leaves a gap in our understanding of the performance trade-offs of quantized models, and it is precisely this gap that our repository aims to fill.

## Why this Repository?

Our independent assessment repository for Open Source Quantized LLMs serves several purposes:

1. **Performance Benchmarks**: We provide benchmarking results for the performance of various open-source quantized LLMs on a range of tasks and datasets, giving an in-depth understanding of their strengths and weaknesses.

2. **Resource Usage Metrics**: We analyze the computational and memory requirements of these quantized models, providing essential insights for practical deployment considerations.

3. **Quantization Trade-off Analysis**: By comparing the performance and resource usage of quantized models with their full-precision counterparts, we quantify the trade-off between model performance and computational efficiency due to quantization.

4. **Community Engagement**: Through open-sourcing this repository, we aim to foster collaboration and encourage the community to contribute their results, driving the further development and refinement of quantized LLMs.


## Benchmarks included:
1. [**hellaswag**](https://github.com/rowanz/hellaswag): Can a Machine Really Finish Your Sentence? 
---

We hope that this repository becomes a valuable resource for the research community, aiding in the development and deployment of efficient and high-performing quantized Large Language Models. Together, let's make LLMs accessible to everyone, everywhere.
