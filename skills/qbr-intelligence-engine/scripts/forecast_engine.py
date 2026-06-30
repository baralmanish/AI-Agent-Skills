"""
Forecast Engine: Generates financial and metric forecasts for QBR
Includes multiple forecasting models for different scenarios
"""

class RevenueForecaster:
    """Generate revenue forecasts based on historical data and leading indicators"""
    
    @staticmethod
    def linear_regression_forecast(historical_quarters, quarters_to_forecast=2):
        """
        Simple linear regression forecast
        Args:
            historical_quarters: List of revenue values [Q1, Q2, Q3, Q4, ...]
            quarters_to_forecast: Number of quarters to project forward
        Returns:
            List of forecasted revenues
        """
        if len(historical_quarters) < 2:
            return []
        
        n = len(historical_quarters)
        x_values = list(range(n))
        y_values = historical_quarters
        
        # Calculate slope and intercept
        x_mean = sum(x_values) / n
        y_mean = sum(y_values) / n
        
        numerator = sum((x_values[i] - x_mean) * (y_values[i] - y_mean) for i in range(n))
        denominator = sum((x_values[i] - x_mean) ** 2 for i in range(n))
        
        if denominator == 0:
            return []
        
        slope = numerator / denominator
        intercept = y_mean - slope * x_mean
        
        # Generate forecast
        forecast = []
        for i in range(n, n + quarters_to_forecast):
            projected = slope * i + intercept
            forecast.append(max(0, projected))
        
        return [round(x, 0) for x in forecast]
    
    @staticmethod
    def growth_rate_forecast(current_revenue, qoq_growth_rate, quarters_to_forecast=2):
        """
        Forecast based on assumed growth rate
        Args:
            current_revenue: Most recent quarter revenue
            qoq_growth_rate: Expected QoQ growth rate (as decimal, e.g., 0.08 for 8%)
            quarters_to_forecast: Number of quarters to project
        Returns:
            List of forecasted revenues
        """
        forecast = []
        revenue = current_revenue
        
        for _ in range(quarters_to_forecast):
            revenue = revenue * (1 + qoq_growth_rate)
            forecast.append(round(revenue, 0))
        
        return forecast
    
    @staticmethod
    def scenario_forecast(current_revenue, upside_rate, base_rate, downside_rate, quarters=2):
        """
        Generate three scenarios: upside, base, downside
        Args:
            current_revenue: Most recent quarter revenue
            upside_rate: Best case QoQ growth
            base_rate: Expected QoQ growth
            downside_rate: Worst case QoQ growth (likely negative)
            quarters: Quarters to forecast
        Returns:
            Dict with upside, base, downside scenarios
        """
        return {
            'upside': RevenueForecaster.growth_rate_forecast(current_revenue, upside_rate, quarters),
            'base': RevenueForecaster.growth_rate_forecast(current_revenue, base_rate, quarters),
            'downside': RevenueForecaster.growth_rate_forecast(current_revenue, downside_rate, quarters)
        }


class ChurnForecaster:
    """Forecast customer churn and retention"""
    
    @staticmethod
    def cohort_retention_forecast(cohort_retention_rates, age_months):
        """
        Predict future retention based on historical cohort patterns
        Args:
            cohort_retention_rates: Dict {age: retention%} for each cohort at age
            age_months: Age in months to forecast
        Returns:
            Predicted retention % at that age
        """
        if not cohort_retention_rates:
            return None
        
        # Average the retention rate at similar ages
        ages = sorted(cohort_retention_rates.keys())
        if age_months <= ages[0]:
            return cohort_retention_rates[ages[0]]
        
        # Simple linear interpolation
        for i in range(len(ages) - 1):
            if ages[i] <= age_months <= ages[i + 1]:
                rate_1 = cohort_retention_rates[ages[i]]
                rate_2 = cohort_retention_rates[ages[i + 1]]
                age_1, age_2 = ages[i], ages[i + 1]
                
                interpolated = rate_1 + (rate_2 - rate_1) * (age_months - age_1) / (age_2 - age_1)
                return round(interpolated, 2)
        
        return cohort_retention_rates[ages[-1]]
    
    @staticmethod
    def churn_rate_forecast(current_churn, trend='stable', quarters=2):
        """
        Forecast churn rate over time
        Args:
            current_churn: Current monthly churn rate (as percentage)
            trend: 'improving', 'stable', or 'deteriorating'
            quarters: Quarters to forecast
        Returns:
            Forecasted monthly churn rates
        """
        forecast = []
        churn = current_churn
        
        trend_delta = {
            'improving': -0.02,      # Improves 2% per month
            'stable': 0,             # No change
            'deteriorating': 0.02    # Worsens 2% per month
        }
        
        delta = trend_delta.get(trend, 0)
        
        for _ in range(quarters * 3):  # 3 months per quarter
            churn = max(0, churn + delta)
            forecast.append(round(churn, 2))
        
        # Return quarterly average
        quarterly = [round(sum(forecast[i*3:(i+1)*3])/3, 2) for i in range(quarters)]
        return quarterly


class OperatingPlanForecaster:
    """Forecast operating expenses and margins"""
    
    @staticmethod
    def headcount_impact_forecast(current_headcount, hiring_plan, cost_per_hire):
        """
        Forecast impact of hiring on operating expenses
        Args:
            current_headcount: Current employee count
            hiring_plan: List of new hires by quarter [Q1, Q2, ...]
            cost_per_hire: Average fully-loaded cost per employee annually
        Returns:
            Quarterly headcount and OpEx impact
        """
        forecast = []
        headcount = current_headcount
        
        for new_hires in hiring_plan:
            headcount += new_hires
            quarterly_opex_impact = (headcount * cost_per_hire) / 4
            forecast.append({
                'headcount': headcount,
                'quarterly_opex': round(quarterly_opex_impact, 0),
                'annual_run_rate_opex': round(headcount * cost_per_hire, 0)
            })
        
        return forecast
    
    @staticmethod
    def margin_forecast(revenue_forecast, cogs_percent, opex_forecast):
        """
        Forecast operating margin
        Args:
            revenue_forecast: List of forecasted revenues
            cogs_percent: COGS as percentage of revenue
            opex_forecast: List of forecasted OpEx amounts
        Returns:
            Forecasted margins and operating income
        """
        forecast = []
        
        for i, revenue in enumerate(revenue_forecast):
            cogs = revenue * (cogs_percent / 100)
            gross_profit = revenue - cogs
            gross_margin = ((revenue - cogs) / revenue) * 100 if revenue > 0 else 0
            
            opex = opex_forecast[i] if i < len(opex_forecast) else opex_forecast[-1]
            operating_income = gross_profit - opex
            operating_margin = (operating_income / revenue) * 100 if revenue > 0 else 0
            
            forecast.append({
                'revenue': round(revenue, 0),
                'cogs': round(cogs, 0),
                'gross_profit': round(gross_profit, 0),
                'gross_margin_pct': round(gross_margin, 1),
                'opex': round(opex, 0),
                'operating_income': round(operating_income, 0),
                'operating_margin_pct': round(operating_margin, 1)
            })
        
        return forecast


if __name__ == "__main__":
    # Example usage
    
    # Revenue forecast
    historical = [1000000, 1200000, 1500000, 1800000]
    forecast = RevenueForecaster.linear_regression_forecast(historical, quarters_to_forecast=2)
    print(f"Linear Regression Forecast: {forecast}")
    
    # Scenario forecast
    scenarios = RevenueForecaster.scenario_forecast(
        current_revenue=1800000,
        upside_rate=0.15,
        base_rate=0.10,
        downside_rate=-0.05,
        quarters=2
    )
    print(f"Scenario Forecast: {scenarios}")
    
    # Churn forecast
    churn_fcst = ChurnForecaster.churn_rate_forecast(current_churn=2.5, trend='improving', quarters=2)
    print(f"Churn Forecast: {churn_fcst}")
    
    # OpEx impact
    headcount_impact = OperatingPlanForecaster.headcount_impact_forecast(
        current_headcount=50,
        hiring_plan=[10, 15, 10],
        cost_per_hire=150000
    )
    print(f"Headcount Impact: {headcount_impact}")
