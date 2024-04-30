<template>
  <div>
    <v-container class="bg-surface-variant">
      <v-row no-gutters>
        <v-col cols="12" sm="4">
          <v-sheet class="ma-2 pa-2">
            <p>Start</p>
            <v-text-field type="date" v-model="eventStartDate" />
            <v-text-field type="time" v-model="eventStartTime" />
            <p>End</p>
            <v-text-field type="date" v-model="eventEndDate" />
            <v-text-field type="time" v-model="eventEndTime" />
            <v-radio-group v-model="selectedOption" row>
              <v-radio label="Start Meeting" value="start"></v-radio>
              <v-radio label="End Meeting" value="end"></v-radio>
            </v-radio-group>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
    <v-btn @click="addEvent">Add Event</v-btn>
    <FullCalendar :options="calendarOptions" />
  </div>
</template>

<script>
import FullCalendar from '@fullcalendar/vue'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'

export default {
  components: {
    FullCalendar
  },
  data() {
    return {
      textTitle: 'ooooo',
      eventStartDate: '',
      eventStartTime: '',
      eventEndDate: '',
      eventEndTime: '',
      selectedOption: '',
      calendarOptions: {
        plugins: [dayGridPlugin, interactionPlugin],
        initialView: 'dayGridMonth',
        dateClick: this.handleDateClick,
        events: [],
        editable: true,
        eventDrop: this.handleEventDrop
      }
    }
  },
  methods: {
    handleDateClick(info) {
      alert('date click! ' + info.dateStr)
    },
    addEvent() {
      if (this.eventStartDate && this.eventStartTime && this.eventEndDate && this.eventEndTime) {
        const eventStartDateTime = `${this.eventStartDate}T${this.eventStartTime}`;
        const eventEndDateTime = `${this.eventEndDate}T${this.eventEndTime}`;

        if (this.selectedOption === 'start') {
          this.calendarOptions.events.push({ title: 'oooo', start: eventStartDateTime });
          this.calendarOptions.events.push({ title: 'oooo', start: eventEndDateTime });
        }

        this.eventStartDate = '';
        this.eventStartTime = '';
        this.eventEndDate = '';
        this.eventEndTime = '';
        this.selectedOption = '';
      } else {
        alert('Please select both start and end date and time.');
      }
    }
  }
}
</script>
