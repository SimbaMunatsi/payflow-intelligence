from src.services.dashboard_service import DashboardService
from src.services.pipeline_service import PipelineService


def main():

    pipeline = PipelineService()

    dashboard = DashboardService()

    result = pipeline.run_pipeline()

    model = dashboard.build_dashboard(
        result
    )

    print()

    print("=" * 60)
    print("DASHBOARD")
    print("=" * 60)

    print(model)


if __name__ == "__main__":

    main()