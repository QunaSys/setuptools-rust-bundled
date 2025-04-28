use pyo3::prelude::*;

#[pyfunction]
fn get_value() -> usize {
    123
}

#[pymodule]
fn example(_py: Python<'_>, m: Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_value, &m)?)?;
    Ok(())
}
