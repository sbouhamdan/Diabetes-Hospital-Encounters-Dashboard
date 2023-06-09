import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import base64
import plotly.express as px
import plotly.graph_objects as go
import altair as alt


# Set Streamlit theme
st.set_page_config(
    page_title="Diabetes Hospital Encounters",
	page_icon="chart_with_upwards_trend",
    layout="wide",
 
)
# Set color palette for visualizations
sns.set_palette("pastel")

# Define the layout
st.title("Diabetes Hospital Encounters Dashboard")

# Add CSS to set the background image for the title
st.markdown(
    """
    <style>
    h1 {
        background-repeat: no-repeat;
        background-color: lightblue;
        background-position: center;
        background-size: cover;
        color: black;
        padding: 1rem;
        text-align: center;
        font-size: 3rem;
    }

    .left-column {
        flex: 1;
        padding-right: 1rem;
        padding-top: 5rem;
    }
    .right-column {
        flex: 1;
        padding-left: 1rem;
    }
	.analytics-text {
			font-size: 1rem;
			text-align: left;
			margin-top: 1rem;
		}

    </style>
    """,
    unsafe_allow_html=True
)
# Load your data
data = pd.read_csv('https://github.com/sbouhamdan/Diabetes-Hospital-Encounters-Dashboard/blob/main/Diabestes_Hospital_Encounters.csv',sep='delimiter')

tab1, tab2, tab3,tab4,tab5 = st.tabs(["Story", "Metrics & Demographics", "Descriptive Analysis","Diagnostic analysis","Overview & definitions"])

with tab1:


	# Create the container with two columns
	col1, col2 = st.columns(2)

	# Add text to the left column
	with col1:
		st.markdown("<div class='left-column'>", unsafe_allow_html=True)
		#st.markdown("<h2 style='background-color: white; padding: 0rem; text-align: left;'>Story</h2>", unsafe_allow_html=True)
		st.write('***Welcome to the Diabetes Hospital Encounter Dashboard*** :sunglasses: !\n')
		st.write("This tool analyzes  **10 years** (1999-2008) of clinical care at **130 US hospitals** and integrated delivery networks for diabetic patients to gain descriptive insights and uncover possible factors that may have impact on hospital readmission within 30 days. ")
		st.write("**11%** of diabetic hospital encounters are seeking inpatient medical care again within 30 days of being discharged. Hospital inpatient care and prescription medications to treat diabetes complications are the largest components of medical expenditures.")
		st.markdown("</div>", unsafe_allow_html=True)

	# Add an image to the right column
	with col2:
		
		st.markdown("<div class='right-column'>", unsafe_allow_html=True)
		image_path = "https://github.com/sbouhamdan/Diabetes-Hospital-Encounters-Dashboard/blob/main/readmission.jpg"  # Replace with the actual path to your image
		st.image(image_path, use_column_width=True)
		st.markdown("</div>", unsafe_allow_html=True)

	# Footer

	# Create the footer container
	with st.container():
		st.markdown("<hr style='border: 1px solid black'>", unsafe_allow_html=True)
		st.text("2023 Healthcare Analytics Dashboard-Samer Bou Hamdan. All rights reserved.")




with tab2:
    # Add your code for tab2 here
    
	# Card section
	with st.container():
		st.markdown(
			"""
			<style>
			.metric-value {
				font-size: 36px;
				color: blue;
			}
			.metric-label {
				font-size: 15px;
				color: black;
				margin-bottom: 0;
				#font-weight: bold;
			}
			</style>
			""",
			unsafe_allow_html=True
		)
		
		# Create five columns for metrics
		col1, col2, col3, col4, col5 = st.columns(5)
		
		# Metric 1: Total hospital Encounters
		with col1:
			st.markdown("<p class='metric-label'>Total Encounters</p>", unsafe_allow_html=True)
			st.markdown(f"<p class='metric-value'>{len(data)}</p>", unsafe_allow_html=True)
		
		# Metric 2: Readmitted = Yes
		with col2:
			readmitted_yes_count = len(data[data['readmitted'] == 'Yes'])
			total_cases = len(data)

			# Calculate the percentage of readmitted cases
			readmitted_percentage = (readmitted_yes_count / total_cases) * 100
			readmitted_percentage_formatted = "{:.2f}%".format(readmitted_percentage)

			st.markdown("<p class='metric-label'>Readmitted</p>", unsafe_allow_html=True)
			st.markdown(f"<p class='metric-value'>{readmitted_percentage_formatted}</p>", unsafe_allow_html=True)
		
		# Metric 3: Average time in hospital
		with col3:
			average_time_in_hospital = data['time_in_hospital'].mean()
			st.markdown("<p class='metric-label'>Avg days in hospital</p>", unsafe_allow_html=True)
			st.markdown(f"<p class='metric-value'>{average_time_in_hospital:.2f}</p>", unsafe_allow_html=True)
		
		# Metric 4: Average lab procedures
		with col4:
			average_lab_procedures = data['num_lab_procedures'].mean()
			st.markdown("<p class='metric-label'>Avg lab procedures/stay</p>", unsafe_allow_html=True)
			st.markdown(f"<p class='metric-value'>{average_lab_procedures:.2f}</p>", unsafe_allow_html=True)
		
		# Metric 5: Average medications
		with col5:
			average_medications = data['num_medications'].mean()
			st.markdown("<p class='metric-label'>Avg medications/stay</p>", unsafe_allow_html=True)
			st.markdown(f"<p class='metric-value'>{average_medications:.2f}</p>", unsafe_allow_html=True)

	# Add a line between sections
	st.markdown("---")

	# Demographics area

	# Create a container for the demographics section
	demographics_container = st.container()

	# Use the container to add content and apply formatting
	with demographics_container:
		
		
		# Create columns for charts
		col1, col2, col3 = st.columns(3)

		# Chart 1: Gender Distribution
		with col1:
			gender_counts = data['gender'].value_counts()

			# Create pie chart
			fig, ax = plt.subplots(figsize=(8, 6))
			wedges, labels, autopct = ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['#2B65EC', '#5CB3FF'])
			# Set plot title and labels
			ax.set_title("Gender\n",fontfamily="Arial", fontsize=18,fontweight='bold')
			# Modify the size of labels
			# Modify the size of labels
			for label in labels:
				label.set_size(8)
			# Show the plot
			st.pyplot(fig)

		# Chart 2: Age Distribution
		with col2:
			# Create countplot
			# Sort the age values in descending order
			sorted_age = data['age'].value_counts().sort_values(ascending=False).index
			fig, ax = plt.subplots(figsize=(8, 6))
			sns.countplot(x="age", data=data,order=sorted_age, palette="Set1")

			# Set plot title and labels
			ax.set_title("Age\n\n\n",fontfamily="Arial",fontsize=24,fontweight='bold')
			ax.set_xlabel("")
			ax.set_ylabel("")
            # Remove the border lines
			ax.spines['top'].set_visible(False)
			ax.spines['right'].set_visible(False)
			ax.spines['bottom'].set_visible(False)
			ax.spines['left'].set_visible(False)
            # Adjust spacing between title and chart
			
			# Show the plot
			st.pyplot(fig)

		# Chart 3: Race Distribution
		with col3:
			# Get the value counts for the race column
			race_counts = data['race'].value_counts()

			# Create a bar chart
			fig, ax = plt.subplots(figsize=(8, 6))
			sns.barplot(x=race_counts.index, y=race_counts.values, color="#1E90FF",ax=ax)

			# Set plot title and labels
			ax.set_title('Race\n\n\n',fontfamily="Arial", fontsize=24,fontweight='bold')
			ax.set_xlabel('')
			ax.set_ylabel('')
            # Remove the border lines
			ax.spines['top'].set_visible(False)
			ax.spines['right'].set_visible(False)
			ax.spines['bottom'].set_visible(False)
			ax.spines['left'].set_visible(False)
			# Rotate the x-axis labels for better readability
			ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

			# Show the plot
			st.pyplot(fig)
			
	

	# Footer

	# Create the footer container
	with st.container():
		st.markdown("<hr style='border: 1px solid black'>", unsafe_allow_html=True)
		st.text("2023 Healthcare Analytics Dashboard-Samer Bou Hamdan. All rights reserved.")



with tab3:
	st.header('*Hospital Encounters*')
	
	# Create the stay_container container
	#stay_container = st.container()


	#with stay_container:
		# Create two columns for line chart and histogram
	col1, col2 = st.columns(2)

	# Line chart: Average time in hospital by age
	with col1:
		# Calculate the average time in the hospital by age
		st.write('')
		average_time = data.groupby('age')['time_in_hospital'].mean().reset_index()

		# Create the line chart using Plotly Express
		fig = px.line(average_time, x='age', y='time_in_hospital')

		# Set the layout properties
		fig.update_layout(
			title='Average Time in Hospital by Age',
			xaxis=dict(title=''),
			yaxis=dict(title=''),
			showlegend=False,
			width=450, height=400
			)

		# Display the line chart in Streamlit
		 
		st.plotly_chart(fig)

		# Histogram: Time in Hospital
	with col2:
			
		# Create the histogram using Plotly
		fig = go.Figure(data=[go.Histogram(
		x=data['time_in_hospital'],
		nbinsx=14,
		marker_color='#73C2FB'
			)])

		# Set the layout properties
		fig.update_layout(
			title='Histogram (days stayed in hospital)',
			xaxis=dict(title=''),
			yaxis=dict(title=''),
			showlegend=False,
			bargap=0.1,
			plot_bgcolor='white'
			,width=450, height=420
			
				#margin=dict(l=10, r=10, t=50, b=10)
			)

			# Display the histogram in Streamlit
		st.plotly_chart(fig)			

	# Create the insight_container container
	encounter_container = st.container()


	with encounter_container:
		# Create two columns 
		col1, col2 = st.columns(2)

        # admission types
		with col1:
		
			admissiontype_counts = data['Admissiontype'].value_counts()

			# Create a DataFrame with the admission type and count values
			admissiontype_data = pd.DataFrame({'Admission Type': admissiontype_counts.index, 'Count': admissiontype_counts.values})

			# Sort the DataFrame by count values in descending order
			admissiontype_data = admissiontype_data.sort_values('Count', ascending=True)

			# Create the horizontal bar chart using plotly.graph_objects
			fig = go.Figure(go.Bar(
				x=admissiontype_data['Count'],
				y=admissiontype_data['Admission Type'],
				orientation='h',
			))

			fig.update_layout(
			title='Admission types',
			#xaxis_title='Count',
			#yaxis_title='Admission Type',
			width=450, height=400,
			#margin=dict(l=100, r=50, t=50, b=50),  # Adjust the margin as per your preference
		)
		
			# Render the plotly figure using st.plotly_chart
			st.plotly_chart(fig)	
		# Discharge category
		with col2:
			st.write('')
			# Create a donut chart using Plotly
			def plot_donut_chart(data):
				# Count the occurrences of each discharge type
				discharge_counts = data["Discharge_type"].value_counts()

				# Create the donut chart using Plotly
				fig = px.pie(discharge_counts, values=discharge_counts.values, names=discharge_counts.index, hole=0.5)

				# Update layout properties
				fig.update_traces(textposition='inside', textinfo='percent+label')
				fig.update_layout(title='Discharge types'
							,width=500, height=400
								)

				# Display the chart using Streamlit
				st.plotly_chart(fig)

			# Call the function to plot the donut chart
			plot_donut_chart(data)
	# Create the insight_container container
	# Add a line between sections
	st.markdown("---")
	st.header('*Medication usage*')
	
	drug_container = st.container()
	st.write('')
	
	with drug_container:	
		
		
		# Create two columns 
		col1, col2 = st.columns([2, 1]) 
		with col1: 
					
			# Filter the data where Diabetes_Med is 'Yes'
			filtered_data = data[data['Diabetes_Med'] == 'Yes']

			# Calculate the count of each medication
			medication_counts = filtered_data['Medication'].value_counts().reset_index()
			medication_counts.columns = ['Medication', 'Count']
			medication_counts = medication_counts.sort_values('Count', ascending=False)

			# Select the top 18 medications
			top_18_medication_counts = medication_counts.head(18)

			

			# Create the Plotly bar chart
			fig = go.Figure(data=[go.Bar(
				x=top_18_medication_counts['Medication'],
				y=top_18_medication_counts['Count'],
			)])

			# Customize the layout
			fig.update_layout(
				title='Top 18 Medications',
				
				xaxis=dict(
					title='',
					tickangle=45,
					tickfont=dict(size=14),
				),
				yaxis=dict(title=''),
				width=800  # Set the width of the chart based on the selected option
			)

			# Render the chart using Plotly in Streamlit
			st.plotly_chart(fig, use_container_width=True)

			
		with col2:
			st.image('https://github.com/sbouhamdan/Diabetes-Hospital-Encounters-Dashboard/blob/main/MedicationCartoon.jpg')
	# Add a line between sections
	st.markdown("---")
	st.header('*Health Condition Diagnosis*')
  

	# treemap for primary diagnosis
	# Calculate the count of each diagnosis value in the filtered data
	diagnosis_counts = data['Diagnosis1'].value_counts()

	# Create a DataFrame with the diagnosis and count values
	diagnosis_data = pd.DataFrame({'Diagnosis': diagnosis_counts.index, 'Count': diagnosis_counts.values})

	# Calculate the percentage of the total count
	diagnosis_data['Percentage'] = diagnosis_data['Count'] / diagnosis_data['Count'].sum() * 100

	# Sort the DataFrame by count in descending order
	diagnosis_data = diagnosis_data.sort_values('Count', ascending=False)

	# Create the treemap using Plotly
	fig = go.Figure(go.Treemap(
		labels=diagnosis_data['Diagnosis'],
		parents=[''] * len(diagnosis_data),
		values=diagnosis_data['Count'],
		texttemplate="%{label}<br>%{value} (%{percentParent})",
		textfont=dict(size=16),
		branchvalues='total',
		hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percentParent}<extra></extra>',
	))

	# Set the title
	fig.update_layout(title='Primary Diagnosis')

	# Display the treemap in Streamlit
	st.plotly_chart(fig, use_container_width=True)
	
	
	with st.container():
		st.markdown("<hr style='border: 1px solid black'>", unsafe_allow_html=True)
		st.text("2023 Healthcare Analytics Dashboard-Samer Bou Hamdan. All rights reserved.")
		
with tab4:
	intro_container = st.container()
	with intro_container:
		# Create two columns for line chart and histogram
		col1, col2 = st.columns(2)

		# Line chart: Average time in hospital by age
		with col1: 
			st.write('')
			st.write('')
			st.write('')
			st.subheader('*Readmission rates significantly influencing hospital quality scores and performance*:sunglasses:')
			
		with col2:
			col1,col2,col3=st.columns(3)
			with col1:
				st.write('')
			with col2: 
				st.image('https://github.com/sbouhamdan/Diabetes-Hospital-Encounters-Dashboard/blob/main/hospital.gif',use_column_width='auto')
			with col3:
				st.write('')
			# create a multi select filter
	
				
	
	col1,col2=st.columns(2)
	with col1: 
		st.write('')
		
		#Calculate the count of each diagnosis value in the readmitted data
		readmitted_data=data[data["readmitted"]=='Yes']
		diagnosis_counts = readmitted_data['Diagnosis'].value_counts().sort_values(ascending=False)

		# Select the top 10 diagnosis values
		top_10_diagnosis = diagnosis_counts[:10]

		# Create a DataFrame with the diagnosis and count values
		diagnosis_data = pd.DataFrame({'Diagnosis': top_10_diagnosis.index, 'Count': top_10_diagnosis.values})

		# Plot the treemap
		fig = px.treemap(diagnosis_data, path=['Diagnosis'], values='Count')

		# Customize the layout
		fig.update_layout(title='Common Commorbodities across readmitted patients'
							 ,width=600, height=400,title_font=dict(size=14))

		# Render the plotly figure using st.plotly_chart
		st.plotly_chart(fig)
	with col2:
	  #Group by A1CResult and calculate the average Num_Outpatient
		avg_num_outpatient = data.groupby(['A1CResult', 'readmitted'])['Num_Outpatient'].mean().reset_index()

		# Create the dot plot using Plotly
		fig = px.scatter(avg_num_outpatient, x='A1CResult', y='Num_Outpatient', color='readmitted',
			 title='Average outpatient visits across A1CResult',
			 labels={'A1CResult': '', 'Num_Outpatient': ''},
			 template='plotly_white',
			 color_discrete_map={'No': 'blue', 'Yes': 'red'},
			 
					 
					# Set the desired height
					)
			# Set the dot size
		fig.update_traces(marker=dict(size=14))
		fig.update_layout(width=600, height=400)
		# Render the plotly figure using st.plotly_chart
		st.plotly_chart(fig)
	# Create the container
	Diagnosis_container = st.container()
	with Diagnosis_container:
	
		col1, col2 ,col3= st.columns(3)

		with col1:
			
			
			readmitted_filter = st.multiselect(
				"Filter by Readmission Status",
				data["readmitted"].unique(),
				default=["Yes"]
			)

			# Apply the filter to the DataFrame
			filtered_data = data[data["readmitted"].isin(readmitted_filter)]
			Medication_Subset = filtered_data[filtered_data['Diabetes_Med'] == 'Yes']
			a1c_change_counts = Medication_Subset.groupby(['A1CResult', 'Change']).size().unstack()

			# Create the side-by-side bar chart using plotly.graph_objects
			fig = go.Figure()

			for col in a1c_change_counts.columns:
				fig.add_trace(go.Bar(
					x=a1c_change_counts.index,
					y=a1c_change_counts[col],
					name=col
				))

			fig.update_layout(
				title='A1CResult with Medication Change',
				xaxis_title='A1C Result',
				yaxis_title='',
				barmode='group'
				,width=450, height=400,
				legend_title_text='Medication Change'
			)

			# Render the plotly figure using st.plotly_chart
			st.plotly_chart(fig)

		with col2: 
			st.write('')
			st.write('')
			st.write('')
			st.write('')
			st.write('')
			st.write('')
			st.write('')
			st.write('')
			st.write('')
			st.write('')
			st.image('https://github.com/sbouhamdan/Diabetes-Hospital-Encounters-Dashboard/blob/main/A1C_charts_approved.png')
		
		with col3: 
			st.write('')
			st.write('')
			st.write('')
			st.write('')
			st.write('')
			
			# Apply filters to create the subset
			filtered_data_subset = filtered_data[(filtered_data['A1CResult'] == '>8') & (filtered_data['Diabetes_Med'] == 'Yes')]

			# Assuming you have a DataFrame called 'data' and the desired columns exist
			columns = ['insulin', 'metformin', 'glimepiride']

			# Calculate the count of each value for each column in the filtered subset
			counts = {}
			for column in columns:
				column_counts = filtered_data_subset[column].value_counts().sort_index()
				counts[column] = column_counts

			# Create a DataFrame with the count values
			count_data = pd.DataFrame(counts)

			# Reset index to make columns as categorical values
			count_data = count_data.reset_index().rename(columns={'index': 'Value'})

			# Melt the DataFrame to convert columns into a single column
			melted_data = count_data.melt(id_vars='Value', var_name='Column', value_name='Count')

			# Plot the count values using a stacked bar chart
			fig = px.bar(melted_data, x='Value', y='Count', color='Column', barmode='stack',
								 labels={'Value': 'Medication Status', 'Count': 'Count'},
								 title='Medicine prescription for severe patients(A1CResult > 8, Med = Yes)')

			fig.update_layout(
						title_font=dict(size=14),width=450, height=400  # Customize the title font size and weight
					)

			# Render the plotly figure using st.plotly_chart
			st.plotly_chart(fig)
					
		
		
	
	# Count the occurrences of each unique value in num_lab_procedures
	col1, col2 = st.columns(2)
	with col1:
		# Filter the data for readmitted = YES and NO
		data2=data[data['Diabetes_Med'] == 'Yes']
		
		
		data_yes = data2[data2['readmitted'] == 'Yes']
		data_no = data2[data2['readmitted'] == 'No']

		# Count the occurrences of each unique value in num_lab_procedures for readmitted = YES and NO
		value_counts_yes = data_yes['num_lab_procedures'].value_counts().sort_index()
		value_counts_no = data_no['num_lab_procedures'].value_counts().sort_index()

		# Create two line traces for readmitted = YES and NO
		trace_yes = go.Scatter(x=value_counts_yes.index, y=value_counts_yes.values, mode='lines', name='Yes')
		trace_no = go.Scatter(x=value_counts_no.index, y=value_counts_no.values, mode='lines', name='No')

		# Create a line chart with both traces
		fig = go.Figure(data=[trace_yes, trace_no])

		# Customize the layout
		fig.update_layout(
			  title= '# of Lab procedures for patients on diabetes medication',
				
			xaxis=dict(title=''),
			yaxis=dict(title='')
			,width=600, height=400,
		)

		# Display the chart using Streamlit
		st.plotly_chart(fig)
	with col2:	
		# Filter the dataset for Diabetes_Med = Yes
		filtered_data = data[data['Diabetes_Med'] == 'Yes']

		# Create a scatter plot with color-coded points
		scatter_plot = px.scatter(filtered_data, x='num_lab_procedures', y='num_medications', color='readmitted',
								  title='Scatter Plot: Number of Lab Procedures vs. Number of Medications',
								  labels={'num_lab_procedures': 'Number of Lab Procedures',
										  'num_medications': 'Number of Medications'},
								  color_discrete_map={'No': 'blue', 'Yes': 'red'})

		# Customize the layout of the scatter plot
		scatter_plot.update_layout(width=600, height=400)

		# Render the plotly figure using st.plotly_chart
		st.plotly_chart(scatter_plot)
	
	
	col1, col2 = st.columns(2)
	with col1:
		# Group the data by 'HospitalStayLength' and 'readmitted', and calculate the count
		grouped_data = data.groupby(['HospitalStayLength', 'readmitted']).size().unstack()

		# Calculate the proportion for each category
		proportion_data = grouped_data.div(grouped_data.sum(axis=1), axis=0)

		# Create the stacked bar chart using Plotly with 'offsetgroup' parameter
		fig = go.Figure(data=[
			go.Bar(name='Not Readmitted', x=proportion_data.index, y=proportion_data['No'], offsetgroup=0),
			go.Bar(name='Readmitted', x=proportion_data.index, y=proportion_data['Yes'], offsetgroup=1, marker_color='red')
		])

		# Set the bar mode to 'relative' for stacked bars
		fig.update_layout(barmode='relative', autosize=True)

		# Set the chart title and axis labels
		fig.update_layout(
			title='Readmission by Hospital Stay Length',
			xaxis_title='',
			yaxis_title='',
			width=600,
			height=400
		)

		# Display the chart on Streamlit app
		st.plotly_chart(fig)
	with col2:
		# Group the data by 'age_group' and 'readmitted', and calculate the count
		grouped_data = data.groupby(['age_group', 'readmitted']).size().unstack()

		# Calculate the proportion for each category
		proportion_data = grouped_data.div(grouped_data.sum(axis=1), axis=0)

		# Create the stacked bar chart using Plotly with 'offsetgroup' parameter
		fig = go.Figure(data=[
			go.Bar(name='Not Readmitted', x=proportion_data.index, y=proportion_data['No'], offsetgroup=0),
			go.Bar(name='Readmitted', x=proportion_data.index, y=proportion_data['Yes'], offsetgroup=1, marker_color='red')
		])

		# Set the bar mode to 'relative' for stacked bars
		fig.update_layout(barmode='relative', autosize=True)

		# Set the chart title and axis labels
		fig.update_layout(
			title='Readmission by Age Group',
				
			xaxis_title='',
			yaxis_title=''
			,width=600, height=400,
		)

		# Display the chart on Streamlit app
		st.plotly_chart(fig)
		
	
	filtered_data = data
	col1, col2 = st.columns([1, 3])
	
	
	with col1:
		# Add the dynamic filters
		st.write('')
		st.write('')
		st.write('')
		st.write('')
		st.write('')
		st.write('')
		st.write('')
		selected_age = st.selectbox('Select Age', ['All'] + data['age'].unique().tolist(), index=0)
		selected_gender = st.selectbox('Select Gender', ['All'] + data['gender'].unique().tolist(), index=0)
		selected_diagnosis = st.selectbox('Select primary Diagnosis', ['All'] + data['Diagnosis1'].unique().tolist(), index=0)
		# Filter the data based on user selections
		# Filter the data based on user selections
		if selected_gender != 'All':
			filtered_data = filtered_data[filtered_data['gender'] == selected_gender]
		if selected_diagnosis != 'All':
			filtered_data = filtered_data[filtered_data['Diagnosis1'] == selected_diagnosis]
		if selected_age != 'All':
			filtered_data = filtered_data[filtered_data['age'] == selected_age]

	with col2:
		# Filter the data for Diabetes_Med = 'Yes'
		filtered_data = filtered_data[filtered_data['Diabetes_Med'] == 'Yes']

		# Group the filtered data by Change, Admissiontype, and readmitted and calculate the count
		grouped_data = filtered_data.groupby(['Change', 'Admissiontype', 'readmitted']).size().reset_index(name='count')

		# Create the stacked bar chart using Plotly Express
		fig = px.bar(grouped_data, x='Change', y='count', color='readmitted', barmode='stack',
					 facet_col='Admissiontype', title='Change, Admission Type, and Readmission Counts for Diabetes_Med = Yes')

		# Set the axis labels
		fig.update_layout(xaxis_title='', yaxis_title='Count')

		# Remove the facet column labels
		fig.update_yaxes(title_text='', showticklabels=False)
		fig.update_xaxes(showticklabels=True, title_text='')

		# Display the chart on Streamlit app
		st.plotly_chart(fig, use_container_width=True)
	with st.container():
		st.markdown("<hr style='border: 1px solid black'>", unsafe_allow_html=True)
		st.text("2023 Healthcare Analytics Dashboard-Samer Bou Hamdan. All rights reserved.")
with tab5: 
	st.write('')
	st.write('')
	st.write('***Overview:***')
	st.write('Information was extracted from the database for encounters that satisfied the following criteria:' )
	st.write('1-It is an inpatient encounter (a hospital admission).')
	st.write('2-It is a diabetic encounter, that is, one during which any kind of diabetes was entered to the system as a diagnosis.')
	st.write('3- Laboratory tests were performed during the encounter.')
	st.write('The data contains such attributes as patient number, race, gender, age, admission type, time in hospital, number of lab test performed, HbA1c test result, diagnosis, number of medication, diabetic medications, number of outpatient, inpatient, and emergency visits in the year before the hospitalization, etc.')
	st.write('***Source:*** The data was found on Kaggle https://www.kaggle.com/datasets/brandao/diabetes?resource=download')
	st.write('***Original data source***: The data are submitted on behalf of the Center for Clinical and Translational Research, Virginia Commonwealth University, a recipient of NIH CTSA grant UL1 TR00058 and a recipient of the CERNER data. John Clore , Krzysztof J. Cios , Jon DeShazo , and Beata Strack . This data is a de-identified abstract of the Health Facts database (Cerner Corporation, Kansas City, MO).')
	st.write('https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008')
	st.write('***Definitions:***')
	st.write('*Outpatient visits*: Clinical visits that a patient makes as a follow up on their health condition')
	st.write('*A1C test*: is a simple blood test that measures your average blood sugar levels over the past 3 months')
	st.write('*A1CResult*: Indicates the range of the result or if the test was not taken. Values: >8 if the result was greater than 8%, >7 if the result was greater than 7% but less than 8%, normal if the result was less than 7%, and none if not measured.')
	st.write('*Number of Lab procedures*: Number of lab tests performed during the encounter')
	st.write('*Number of Medications*: Number of distinct generic names administered during the encounter')
	st.write('*Long Stay*: Stay in hospital > 6 days')
	st.write('*Short Stay*: Stay in hospital <= 6 days')
	st.write('*Adolescents*: population with age range 0-10')
	st.write('*Teenagers*: population with age range 10-20')
	st.write('*Young adults*: population with age range 20-30')
	st.write('*Middle adults*: population with age range 30-50')
	st.write('*Seniors*: population with age range 50-100')
	with st.container():
		st.markdown("<hr style='border: 1px solid black'>", unsafe_allow_html=True)
		st.text("2023 Healthcare Analytics Dashboard-Samer Bou Hamdan. All rights reserved.")