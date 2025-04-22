use pyo3::prelude::*;

#[pymodule]
fn example(_py: Python<'_>, _m: Bound<'_, PyModule>) -> PyResult<()> {
    Ok(())
}
