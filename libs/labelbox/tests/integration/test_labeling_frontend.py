import pytest
from lbox.exceptions import OperationNotSupportedException

from labelbox import LabelingFrontend


def test_get_labeling_frontends(client):
    filtered_frontends = list(
        client._get_labeling_frontends(where=LabelingFrontend.name == "Editor")
    )
    assert len(filtered_frontends)


def test_labeling_frontend_connecting_to_project(project):
    client = project.client
    default_labeling_frontend = next(
        client._get_labeling_frontends(where=LabelingFrontend.name == "Editor")
    )

    assert project.labeling_frontend() is None

    project.labeling_frontend.connect(default_labeling_frontend)
    assert project.labeling_frontend() == default_labeling_frontend

    with pytest.raises(OperationNotSupportedException):
        project.labeling_frontend.disconnect(default_labeling_frontend)
