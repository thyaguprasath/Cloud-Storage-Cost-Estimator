
# cloud_cost_estimator.py

class CloudCostEstimator:
    def __init__(self):
        self.providers = {
            'AWS': 0.023,  # cost per GB per month in USD
            'Azure': 0.02,
            'Google Cloud': 0.021
        }

    def estimate_storage_cost(self, provider, gb_used):
        """Estimate cost based on provider and GB used."""
        if provider not in self.providers:
            raise ValueError('Provider not supported')
        cost_per_gb = self.providers[provider]
        return gb_used * cost_per_gb


def main():
    estimator = CloudCostEstimator()

    print('Cloud Storage Cost Estimator')
    print('Supported providers: AWS, Azure, Google Cloud')

    provider = input('Enter cloud provider: ')
    gb_used = float(input('Enter storage used (in GB): '))

    try:
        cost = estimator.estimate_storage_cost(provider, gb_used)
        print(f'Estimated monthly cost for {gb_used} GB on {provider}: ${cost:.2f}')
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
