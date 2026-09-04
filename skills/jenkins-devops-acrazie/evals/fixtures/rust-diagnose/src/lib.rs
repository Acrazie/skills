pub fn total(values: &[u64]) -> u64 {
    values.iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn totals_values() {
        assert_eq!(total(&[2, 3]), 5);
    }
}
