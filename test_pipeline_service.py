from src.services.pipeline_service import PipelineService


def main():

    service = PipelineService()

    result = service.run_pipeline()

    print()

    print("=" * 60)
    print("PIPELINE SERVICE")
    print("=" * 60)

    for key, value in result.items():

        print(f"{key:<30}{value}")


if __name__ == "__main__":
    main()