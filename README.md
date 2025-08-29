# Cloud Storage Cost Estimator

A simple command-line tool built in Python to estimate and compare the monthly costs of object storage across major cloud providers: AWS, Azure, and Google Cloud.

## Description

This tool provides a basic cost estimation for cloud object storage based on the amount of data (in GB). It's designed to give a quick comparison for developers and students learning about cloud services and their pricing models.

## How to Use

1.  Clone this repository or download the `cloud_cost_estimator.py` file.
2.  Run the script from your terminal:
    ```
    python cloud_cost_estimator.py
    ```
3.  Follow the on-screen prompts to enter the cloud provider and the storage amount in GB.

## Features

-   **Supported Providers**: AWS, Azure, and Google Cloud.
-   **Calculation**: Estimates cost based on per-gigabyte monthly rates.
-   **Extensible**: The class-based structure makes it easy to add more providers or services.

**Disclaimer**: The pricing used in this tool is for estimation purposes only and may not reflect the most current rates. Always refer to the official documentation of the cloud providers for accurate pricing.
