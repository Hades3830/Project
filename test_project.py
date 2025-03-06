import pytest
import project

def test_add_expense():
    assert project.add_expense(20, "Food", "2025-03-02") == True

def test_view_expenses():
    expenses = project.view_expenses()
    assert isinstance(expenses, list)

def test_total_expenses():
    project.add_expense(10, "Transport", "2025-03-02")
    project.add_expense(15, "Food", "2025-03-03")
    assert project.total_expenses() >= 25  # Total should be at least 25